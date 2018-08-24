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
    def delete_credentials(self):
        '''
        method to delete credentials from credentials_list
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_credentials_by_platform_name(cls,platform_name):
        '''
        method to search through the credentials_listby platform name and return the credentials
        '''
        for credentials in cls.credentials_list:
            if credentials.platform_name == platform_name:
                return credentials
