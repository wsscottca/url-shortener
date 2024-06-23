# URL Shortener API

Welcome to the URL Shortener API! This FastAPI application allows you to shorten URLs, list all shortened URLs, redirect using short URLs, and manage user authentication and authorization.

## Table of Contents

- [Routes](#routes)
  - [Root](#root)
  - [Shorten URL](#shorten-url)
  - [List URLs](#list-urls)
  - [Redirect](#redirect)
  - [User Authentication](#user-authentication)
    - [Login](#login)
    - [Signup](#signup)
    - [Get Current User](#get-current-user)
- [Usage Examples](#usage-examples)

The API is deployed at [https://shrtnurl.com/](https://shrtnurl.com/) and the interactive documentation is available at [https://shrtnurl.com/docs](https://shrtnurl.com/docs).

## Routes

### Root

**GET /**

- **Description**: This route serves as the entry point to the API and provides a basic message to indicate that the API is running.
- **Response**: A JSON object with a welcome message.
- **Example Response**:
  ```json
  {
    "message": "URL Shortener API"
  }
  ```

### Shorten URL

**POST /shorten_url**

- **Description**: This route allows users to shorten a given valid URL. Users can optionally provide their own short URL code, otherwise, a unique short URL code will be generated.
- **Attributes**:
  - `url` (HttpUrl): The valid web address that needs to be shortened.
  - `short_url` (Optional[str]): An optional short URL code to use (maximum length 8 characters). If not provided, a unique short URL will be generated.
- **Response**: A JSON object containing the original URL and the newly created short URL.
- **Example Response**:
  ```json
  {
    "short_url": "https://shrtnurl.com/shorty",
    "url": "http://example.com"
  }
  ```

### List URLs

**GET /list_urls**

- **Description**: This route allows authenticated users with the necessary permissions (admin role) to retrieve a list of all shortened URLs in the system.
- **Attributes**:
  - `token` (oauth2_scheme): The Bearer token used for authentication and authorization.
- **Response**: A JSON object containing the URL pairs with their short and original URLs.
- **Example Response**:
  ```json
  {
    "shorty1": "http://example1.com",
    "shorty2": "http://example2.com"
  }
  ```

### Redirect

**GET /{short_url}**

- **Description**: This route handles the redirection of users from a short URL to the original URL. When a user accesses a short URL, they are redirected to the corresponding original URL.
- **Attributes**:
  - `short_url` (str): The short URL code (maximum length 8 characters).
- **Response**: A redirection response that takes the user to the original URL associated with the short URL.
- **Example Response**: The user is redirected to `http://example.com` if they access `https://shrtnurl.com/shorty`.

### User Authentication

#### Login

**POST /token**

- **Description**: This route allows users to log in using their username and password. Upon successful authentication, the user receives a JWT token for subsequent authorized requests.
- **Attributes**:
  - `form_data` (OAuth2PasswordRequestForm): The form data containing the username and password for the Password OAuth2 flow.
- **Response**: A JSON object containing the access token and the token type.
- **Example Response**:
  ```json
  {
    "access_token": "eyJhbGciOi...",
    "token_type": "bearer"
  }
  ```

#### Signup

**POST /signup**

- **Description**: This route allows new users to create an account by providing a username and password. The username must be unique, and the password must meet the length requirements.
- **Attributes**:
  - `username` (str): The username for the new account (between 4-16 characters).
  - `password` (str): The password for the new account (between 8-32 characters).
- **Response**: A JSON object confirming the creation of the new user.
- **Example Response**:
  ```json
  {
    "username": "newuser",
    "msg": "User created successfully"
  }
  ```

#### Get Current User

**GET /users/me**

- **Description**: This route allows authenticated users to retrieve information about their own account.
- **Attributes**:
  - `current_user` (User): The current authenticated user.
- **Response**: A JSON object containing the current user's information.
- **Example Response**:
  ```json
  {
    "username": "currentuser",
    "group": "user",
    "disabled": false
  }
  ```

## Usage Examples

### Shorten a URL

```bash
curl -X POST "https://shrtnurl.com/shorten_url" -d "url=http://example.com"
```

- **Description**: This command sends a POST request to the `shorten_url` route with the URL to be shortened as a parameter. The API responds with a JSON object containing the original URL and the newly created short URL.

**Response:**
```json
{
  "short_url": "https://shrtnurl.com/shorty",
  "url": "http://example.com"
}
```

### List URLs

```bash
curl -H "Authorization: Bearer your_token" "https://shrtnurl.com/list_urls"
```

- **Description**: This command sends a GET request to the `list_urls` route with an authorization token. The API responds with a JSON object containing the URL pairs with their short and original URLs.

**Response:**
```json
{
  "shorty1": "http://example1.com",
  "shorty2": "http://example2.com"
}
```

### Redirect

```bash
curl -L "https://shrtnurl.com/shorty"
```

- **Description**: This command sends a GET request to the `redirect` route with the short URL as a parameter. The user is redirected to the original URL associated with the short URL.

### Login

```bash
curl -X POST "https://shrtnurl.com/token" -d "username=user&password=pass"
```

- **Description**: This command sends a POST request to the `login` route with the username and password as parameters. The API responds with a JSON object containing the access token and the token type.

**Response:**
```json
{
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}
```

### Signup

```bash
curl -X POST "https://shrtnurl.com/signup" -d "username=newuser&password=newpass"
```

- **Description**: This command sends a POST request to the `signup` route with the username and password as parameters. The API responds with a JSON object confirming the creation of the new user.

**Response:**
```json
{
  "username": "newuser",
  "msg": "User created successfully"
}
```

### Get Current User

```bash
curl -H "Authorization: Bearer your_token" "https://shrtnurl.com/users/me"
```

- **Description**: This command sends a GET request to the `users/me` route with an authorization token. The API responds with a JSON object containing the current user's information.

**Response:**
```json
{
  "username": "currentuser",
  "group": "user",
  "disabled": false
}
```
