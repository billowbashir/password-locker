class Credentials:
    '''
    class that generates new instance of the credential details
    '''
    credentials_list = []

    def __init__(self,platform_name,username,password):
        self.platform_name=platform_name
        self.username=username
        self.password=password


    def save_credentials(self):
        '''
        method to save credentials to credentials_list
        '''
        Credentials.credentials_list.append(self)    
