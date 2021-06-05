# SocialNetworkAPI
# Installation <br/>
#### `Install requirements:` <br/>
1. Simply run  pip install -r requirements.txt (or pip3 install -r requirements.txt if you're on linux) <br/>
2. Clone repository: <br/>
git clone https://github.com/lyyubava/SocialNetworkAPI<br/>
3. cd SocialNetworkAPI<br/>
`Configure db in config.py` <br/>
# Overview of API methods
# User signup  <br/>

#### `POST /api/users/signup` 

###  Example:  <br/>

`curl -X POST -H "Content-Type: application/json" -d '{"first_name": "Test first name", "last_name":"Test last name", "email": "test@email.com", "password":"test password", "username":"testusername"}'  localhost:5000/api/users/signup` <br/>

Fields first_name, last_name, email, username, password can not be blank. Also username must be unique. Otherwise you will get the following response:
` {
  "code": "InvalidInput", 
  "message": "Invalid input"
} `

# User login  <br/>
#### `POST /api/users/login`

###  Example:  <br/>

`curl -X POST -H "Content-Type:application/json" -d '{"password":"test password", "username":"testusername"}' localhost:5000/api/users/login`

In case of successful login, you will get following output

` {
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMjgzOTk2NiwianRpIjoiM2YwMTk0ZGItYmU5MS00ZmVhLThhMTUtYTUzNzI3NTIzNmE3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OSwibmJmIjoxNjIyODM5OTY2LCJleHAiOjE2MjI4NDA4NjZ9.HWJMPDyZayVnHODXRAAsoG9GEQj6YYlpu5AaU1aeCv4", 
  "code": "success", 
  "message": "Logged in as testusername"
} `

# Post creation  <br/>
#### `POST /api/users/create_post` 
 
###  Example: <br/>

`curl -H  "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMjg0MDkxMiwianRpIjoiNTM3ZjczY2YtZDZlMS00YzQyLTkxNjAtNGJjOGQ0OTY0MmFkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OSwibmJmIjoxNjIyODQwOTEyLCJleHAiOjE2MjI4NDE4MTJ9.C5mlBuFFFuIG-pNFIFeyQ57ecw4tyIq6ra6rqqghC1w" -X POST -H "Content-Type: application/json" -d '{"title":"test title"}' localhost:5000/api/users/create_post`

# Post like/unlike
#### `POST /api/like_post/like.delete or POST /api/like_post/like.add`

###  Example: <br/>

`curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyMjg0NTIxNiwianRpIjoiYmE2MjNlYjUtMjMzZC00ZjE3LWFmNTQtMzAzYjMzNmJmYTBlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OSwibmJmIjoxNjIyODQ1MjE2LCJleHAiOjE2MjI4NDYxMTZ9.9F8SoOxyEhJhsbeVxWRL95dRbnmLdjN2sxY3ck_LxQo" -X POST -H "Content-Type: application/json" -d'{"post_id": 2}' localhost:5000/api/like_post/like.add`

# Analytics about how many likes was made aggregated by day.
#### `GET /api/analytics/likes`

###  Example: <br/>

`curl -X GET -H "Content-Type: application/json" -d '{"date_from": "2012-12-12", "date_to": "2021-12-12"}' localhost:5000/api/analytics/likes`

` {
  "code": "success", 
  "total amount of likes from 2012-12-12 to 2021-12-12": {
    "2021-06-02": 2, 
    "2021-06-04": 5, 
    "2021-06-05": 1
  }
} `

# User activity an endpoint which will show when user was login last time and when he made a last request to the service
#### `GET /api/analytics/<username>/activity`

###  Example: <br/>

`curl -X GET -H "Content-Type: application/json" -d '{"date_from": "2012-12-12", "date_to": "2021-12-12"}' localhost:5000/api/analytics/testusername/activity`

` {
  "code": "success", 
  "history_of_requests": [
    {
      "2021-06-05 01:23:44": "like_action"
    }, 
    {
      "2021-06-05 01:23:39": "like_action"
    }, 
    {
      "2021-06-05 01:23:27": "like_action"
    }, 
    {
      "2021-06-05 01:23:05": "like_action"
    }, 
    {
      "2021-06-05 01:22:49": "like_action"
    }, 
    {
      "2021-06-05 01:18:45": "like_action"
    }, 
    {
      "2021-06-05 01:16:22": "like_action"
    }, 
    {
      "2021-06-05 01:12:44": "like_action"
    }, 
    {
      "2021-06-05 01:10:47": "like_action"
    }, 
    {
      "2021-06-05 01:10:03": "like_action"
    }, 
    {
      "2021-06-05 01:09:21": "like_action"
    }, 
    {
      "2021-06-05 01:07:48": "like_action"
    }, 
    {
      "2021-06-05 01:07:17": "like_action"
    }, 
    {
      "2021-06-05 01:06:38": "like_action"
    }, 
    {
      "2021-06-05 01:05:14": "like_action"
    }, 
    {
      "2021-06-05 00:19:46": "create_post"
    }, 
    {
      "2021-06-05 00:17:59": "create_post"
    }, 
    {
      "2021-06-05 00:13:39": "create_post"
    }, 
    {
      "2021-06-05 00:09:27": "create_post"
    }, 
    {
      "2021-06-05 00:09:18": "create_post"
    }, 
    {
      "2021-06-05 00:08:57": "create_post"
    }, 
    {
      "2021-06-05 00:06:03": "create_post"
    }
  ], 
  "last login of testusername": "Fri, 04 Jun 2021 23:52:47 GMT"
}
 `
# Get info about user and its post  <br/>
#### `GET /api/users/<username>`
###  Example: <br/>
` curl -X GET localhost:5000/api/users/testusername `

`{
  "code": "success", 
  "user": {
    "email": "test@email.com", 
    "first_name": "Test first name", 
    "last_name": "Test last name"
  }
}`
#### `GET /api/users/<username>/posts `
###  Example: <br/>
` curl -X GET localhost:5000/api/users/lyyubava/posts `

` {
  "code": "success", 
  "post": [
    {
      "created": "2021-05-29T04:08:30", 
      "likes": 12, 
      "title": "try1"
    }, 
    {
      "created": "2021-05-31T00:37:34", 
      "likes": 1, 
      "title": "try2"
    }, 
    {
      "created": "2021-06-01T16:53:45", 
      "likes": 2, 
      "title": "New title"
    }
  ]
} `










