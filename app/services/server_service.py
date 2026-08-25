

"""
This file is used to interact with the server and perform various operations related to server management. It contains functions and classes that handle server requests, responses, and other server-related tasks.
"""


class ServerService:
    def __init__(self , server_url : str):
        self.server_url = server_url

    def get_server_status(self) -> dict:
        """
        This function is used to get the status of the server. It sends a request to the server and returns the response.
        """
        # send a request to the server to get the status
        response = requests.get(f"{self.server_url}/status")
        
        # return the response as a dictionary
        return response.json()

    async def send_token_to_server(self , token : str ):
        """
        This function is used to send the tokn to the server 
        """

        # Token payload 
        request_payload = {
            "token" : token 
        }

        response = await requests.post(f"{self.server_url}/node-registration" , json = request_payload)

        if response.status_code != 200 :
            raise ServerErrorException(f"Failed to send token to server. Status code: {response.status_code}, Response: {response.text}") 
        


if __name__ == "__main__":
    server_service = ServerService("http://localhost:8000")
    status = server_service.get_server_status()
    print(status)