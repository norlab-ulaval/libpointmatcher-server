## Database

### Technologies

We are using Mongo for the database.

### Database

#### Users
The application saves the data of users, like the username or the email. The password is encrypted
to make sure the information and the account is secure.

We are saving the information as a document. The document uses the format : 
```
user_json = {
    "username": str,
    "email": str,
    "password": str
}
```

#### Leaderboard and evaluations

The application saves the data of each evaluation done when uploading a configuration
to be evaluated by the librairy.

The format saved for the evaluation is :
```
evaluation = {
    "run_id" : str,
    "user_email" : str,
    "type" : str,
    "evaluation_name" : str,
    "file_name" : str,
    "iterations" : list[iterations],
    "date" : datetime,
    "anonymous" : bool
}
```

The data for the leaderboard is slightly different. This data is saved when the users upload new configurations
and if the rotation errors and the translation errors are better.

The format is :
```
leaderboard_entry = {
    file_name: str
    type: str
    user_email: str
    rotation_error: float
    translation_error: float
    date: datetime
    release_version: str
    anonymous: bool
}
```