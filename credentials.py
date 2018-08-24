class Credentials:
    '''
    class that generates new instance of the credential details
    '''
    credentials_list = []

    def _init_(self,platform_name,username,password):
        self.platform_name=platform_name
        self.username=username
        self.password=password
