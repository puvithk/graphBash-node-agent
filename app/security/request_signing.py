# The system ask the user to put the token then the token is send to the server to verify if the token is valid or not. If the token is valid then the user can access the system otherwise the user will be denied access.

# The windows returns api ey then the information about the complete system is sent to the server to verify if the api key is valid or not. If the api key is valid then the user can access the system otherwise the user will be denied access.



# The basic details are sent to the server to verify if the user is valid or not. 

class RequestSigning:
    def __init__(self):
        self.api_key = None 


    async def _verify_token(token : str ) -> bool :
        """
        Takes the token as input and request the server to verify if the token is valid or not 
        """

        # send the token to the server to verify if the token is valid or not
        response = await send_token_to_server(token)
        
        # if the token is valid then return True otherwise return False
        if response.status_code == 200:
            self.api_key = response.json().get("api_key")
            return True
        else:
            return False
        

    


