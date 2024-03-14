## Database

### Technologies

Currently, we are using Mongo for the database.

### Database

The application will save the data of users, like the username or the email. The password is encrypted
to make sure the information and the account is secure.

We are saving the information as a document. The document uses a format like : 
```
user_json = {
    "username": username,
    "email": email,
    "password": password
}
```