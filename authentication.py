import boto3
import hmac
import hashlib
import base64

USER_POOL_ID = 'ap-south-1_k3icS362X'
CLIENT_ID = '7741f2ueeh3gkvdh1thrrcqlm7'
CLIENT_SECRET = '1qnn95pj0qdpfvm2tlesf248qboufi380r974uam1rmsfjsbr3rg'


def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'),
        msg=str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2


def sign_up(data):
    client = boto3.Session(
            aws_access_key_id="AKIA34ZDFDGVCNH7TWHP",
            aws_secret_access_key="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",
            region_name="ap-south-1"
        ).client('cognito-idp')
    try:
        resp = client.sign_up(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(data.user_name),
            Username=data.user_name,
            Password=data.password,
        )
        return None, resp
    except client.exceptions.UsernameExistsException as e:
        return {"error": False,
               "success": True,
               "message": "This username already exists",
               "data": None}, None
    except client.exceptions.InvalidPasswordException as e:

        return {"error": False,
               "success": True,
               "message": "Password should have Caps,\
                          Special chars, Numbers",
               "data": None}, None
    except client.exceptions.UserLambdaValidationException as e:
        return {"error": False,
               "success": True,
               "message": "Email already exists",
               "data": None}, None

    except Exception as e:
        return {"error": False,
                "success": True,
                "message": str(e),
               "data": None}, None


def login(data):
    client = boto3.Session(
            aws_access_key_id="AKIA34ZDFDGVCNH7TWHP",
            aws_secret_access_key="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",
            region_name="ap-south-1"
        ).client('cognito-idp')
    secret_hash = get_secret_hash(data.user_name)
    try:
        resp = client.admin_initiate_auth(
            UserPoolId=USER_POOL_ID,
            ClientId=CLIENT_ID,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': data.user_name,
                'SECRET_HASH': secret_hash,
                'PASSWORD': data.password,
            },
            ClientMetadata={
                'username': data.user_name,
                'password': data.password,
            })
        return None, resp
    except client.exceptions.NotAuthorizedException:
        return None, "The username or password is incorrect"
    except client.exceptions.UserNotConfirmedException:
        return None, "User is not confirmed"
    except Exception as e:
        return None, e.__str__()


def confirm_signup(data):
    client = boto3.Session(
            aws_access_key_id="AKIA34ZDFDGVCNH7TWHP",
            aws_secret_access_key="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",
            region_name="ap-south-1"
        ).client('cognito-idp')
    try:
        response = client.confirm_sign_up(
        ClientId=CLIENT_ID,
        SecretHash=get_secret_hash(data.username),
        Username=data.username,
        ConfirmationCode=data.code,
        ForceAliasCreation=False,
        )
        return None, response
    except client.exceptions.UserNotFoundException:
        return {"error": True, "success": False, "message": "Username doesnt exists"}
        # return event
    except client.exceptions.CodeMismatchException:
        return {"error": True, "success": False, "message": "Invalid Verification code"}
        
    except client.exceptions.NotAuthorizedException:
        return {"error": True, "success": False, "message": "User is already confirmed"}
    
    except Exception as e:
        return {"error": True, "success": False, "message": f"Unknown error {e.__str__()} "}


def forget_password(data):
    # client = boto3.client('cognito-idp')
    try:
        client = boto3.Session(
            aws_access_key_id="AKIA34ZDFDGVCNH7TWHP",
            aws_secret_access_key="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",
            region_name="ap-south-1"
        ).client('cognito-idp')
        response = client.forgot_password(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(data),
            Username=data
        )
        print(response)
        return None, "Please check your Registered email id for validation code"
    except client.exceptions.UserNotFoundException:
        return {"error": True, 
                "data": None, 
                "success": False, 
                "message": "Username doesnt exists"}, None

    except client.exceptions.InvalidParameterException:
        return {"error": True, 
                "success": False,
                "data": None, 
              "message": f"User <{data.username}> is not confirmed yet"}, None
    
    except client.exceptions.CodeMismatchException:
        return {"error": True, 
                "success": False, 
                "data": None, 
                "message": "Invalid Verification code"}, None
        
    except client.exceptions.NotAuthorizedException:
        return {"error": True, 
                "success": False,
                "data": None, 
                "message": "User is already confirmed"}, None
    
    except Exception as e:
        return {"error": True, 
                "success": False, 
                "data": None, 
                "message": f"Uknown    error {e.__str__()} "}, None
    

def confirm_forget_password(data):
    client = boto3.Session(
            aws_access_key_id="AKIA34ZDFDGVCNH7TWHP",
            aws_secret_access_key="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",
            region_name="ap-south-1"
        ).client('cognito-idp')
    try:
        client.confirm_forgot_password(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(data.username),
            Username=data.username,
            ConfirmationCode=data.code,
            Password=data.password,
           )
        return None, "Password has been changed successfully"
    except client.exceptions.UserNotFoundException as e:
        return {"error": True, 
                "success": False,
                "data":  None,
                "message": "Username doesnt exists"}, None
        
    except client.exceptions.CodeMismatchException as e:
            return {"error": True, 
                "success": False,
                "data": None,
                "message": "Invalid Verification code"}, None
        
    except client.exceptions.NotAuthorizedException as e:
        return {"error": True, 
                 "success": False, 
                 "data": None, 
                 "message": "User is already confirmed"}, None
    
    except Exception as e:
        return {"error": True, 
                "success": False,
                "data": None,
                "message": f"Unknown error {e.__str__()} "}, None


