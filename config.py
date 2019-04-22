class SmtpConfig:

    def __init__(self, server, port, user_name, password):
        self.server = server
        self.port = port
        self.user_name = user_name
        self.password = password


connection = SmtpConfig('smtp.gmail.com', 587, 'XXXX@gmail.com', 'PASSXXX')
