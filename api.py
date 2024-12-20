from linkedin_api.clients.restli.client import RestliClient
import os

def get_linkedin_response():
  ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
  restli_client = RestliClient()

  response = restli_client.get(
    resource_path="/userinfo",
    access_token=ACCESS_TOKEN
  )
  print(response.entity)
  return response.entity
