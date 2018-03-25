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
- :white_large_square: Forms
- :white_large_square: Landing Pages
- :white_large_square: Tracking
- :white_large_square: List
- :white_large_square: Email

## Production Check

- Debug False
- Production Database
- Production SendGrid API
- Paid Dyno
- Metrics Enabled

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
### Landing Pages
### Emails

## Credits
Created by [Vaibhav Sharma](https://github.com/v4iv/) for [Inbound Mantra](https://www.inboundmantra.com/).