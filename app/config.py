from pydantic_settings import BaseSettings


# dealing with environment variables 
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str 
    access_token_expiration_time: int 
    admin_email: str 
    admin_password: str 

    zoho_smtp_sender_email: str 
    zoho_smtp_username: str 
    zoho_smtp_outgoing_server_name: str 
    zoho_smtp_password: str 
    zoho_smtp_port_with_tls: int 
    zoho_smtp_port_with_ssl: int 
    zoho_smtp_require_authentication: str 



    class Config:
        env_file = ".env"

settings = Settings()

