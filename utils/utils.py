from linkedin_api import Linkedin

# הזנת פרטי התחברות לחשבון LinkedIn שלך
username = "tut96740@gmail.com"
password = "Tuti1234"

# התחברות ל-LinkedIn API
api = Linkedin(username, password)

# פונקציה לחיפוש חברות בישראל עם פחות מ-500 עובדים
def search_companies_in_israel(max_results=100, max_employees=500):
    results = []
    seen_companies = set()
    location = "Israel"

    # חיפוש חברות והגבלת מספר התוצאות מראש
    search_results = api.search({"keywords": location, "entityType": "Company"})[
                     :max_results * 2]  # מחזירים כפול תוצאות למקרה של סינון בהמשך

    for result in search_results:
        if len(results) >= max_results:
            break

        if result.get("__typename") == "Company":
            urn_id = result.get("urn_id")
            if urn_id and urn_id not in seen_companies:
                seen_companies.add(urn_id)

                # בדיקת פרטי החברה
                try:
                    company_details = api.get_company(urn_id)

                    # בדיקת מספר העובדים
                    if "staffCountRange" in company_details:
                        employees_range = company_details["staffCountRange"]
                        if employees_range.get("start", 0) < max_employees:
                            results.append({
                                "name": company_details.get("name"),
                                "industry": company_details.get("industryName", "Unknown"),
                                "size": employees_range,
                                "location": company_details.get("confirmedLocations", [{}])[0].get("city", "Unknown"),
                            })
                except Exception as e:
                    print(f"Error fetching company details for URN ID {urn_id}: {e}")

    return results

print(f"Start")

# חיפוש והדפסת תוצאות
companies = search_companies_in_israel()

for company in companies:
    print(f"Name: {company['name']}, Industry: {company['industry']}, Employees: {company['size']}, Location: {company['location']}")

print(f"END")