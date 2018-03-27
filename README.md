# MakeSamai
REST API backend for MakeSamai.

## Stack
- Django
- Postgres
- Gunicorn
- Amazon S3 Storages
- Heroku

## Modules
- :heavy_check_mark: User and Authentication
- :heavy_check_mark: Accounts
- :heavy_check_mark: Contact
- :heavy_check_mark: Forms
- :heavy_check_mark: Landing Pages
- :heavy_check_mark: List
- :white_large_square: Email
- :white_large_square: Tracking

## Deployment CheckList

- :white_large_square: Debug False
- :white_large_square: Production Database
- :white_large_square: Production SendGrid API
- :white_large_square: Production Dyno
- :white_large_square: Metrics Enabled

## Important Commands

To create migrations

```python manage.py makemigrations```

To run migrations on the database

```python manage.py migrate```

To create a superuser

```python manage.py createsuperuser```

## Root URL

http://api.makesamai.com

## API Endpoints
Suffix ```?format=json``` on get apis to get JSON format data.

### Clients
#### Create

```/api/signup/```

Authentication Required - *False*

Method Allowed - *POST*

#### Authenticate

```/api/o/token/```

Authentication Required - *N/A*

Method Allowed - *POST*

### Accounts
#### Create

#### User Accounts List Create

```/api/account/```

Authentication Required - *True*

Method Allowed - *GET, POST*

#### Account Retrieve/Update/Destroy

```/api/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET, PUT, PATCH, DELETE*

### Contacts
#### Address Create

```/api/address/create/```

Authentication Required - *False*

Method Allowed - *POST*

#### Address Retrieve/Update/Destroy

```/api/address/<address_id>/```

Authentication Required - *False*

Method Allowed - *GET, PUT, PATCH, DELETE*

#### Contact List

```/api/contact/list/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET*

#### Contact Create


```/api/contact/create/```

Authentication Required - *False*

Method Allowed - *POST*

#### Contact Retrieve/Update/Destroy

```api/contact/retrieve/<contact_id>/account/<account_id>/```

Authentication Required - *False*

Method Allowed - *GET, PUT, PATCH, DELETE*

### Forms
#### List/Create

```/api/form/list/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET, POST*

#### Retrieve/Update/Destroy

```/api/form/retrieve/<form_id>/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET, PUT, PATCH, DELETE*


#### Render

```/api/form/render/<form_id>/account/<account_id>/```

Authentication Required - *False*

Method Allowed - *GET*

### Landing Pages
#### List/Create

```/api/landing_page/list/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET, POST*

#### Retrieve/Update/Destroy

```/api/landing_page/retrieve/<landing_page_id>/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET, PUT, PATCH, DELETE*


#### Render

```/api/landing_page/render/<landing_page_id>/account/<account_id>/```

Authentication Required - *False*

Method Allowed - *GET*

### Lists
#### List/Create

```/api/list/list/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET, POST*

#### Retrieve/Update/Destroy

```/api/list/retrieve/<list_id>/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET, PUT, PATCH, DELETE*

### Emails
### Trakcing

## Credits
Created by [Vaibhav Sharma](https://github.com/v4iv/) for [Inbound Mantra](https://www.inboundmantra.com/).