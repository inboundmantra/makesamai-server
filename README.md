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

## API Endpoints
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

```/api/account/create/```

Authentication Required - *True*

Method Allowed - *POST*

#### User Accounts List

```/api/account/u/<user_id>/```

Authentication Required - *True*

Method Allowed - *GET*

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

#### Contact Create


```/api/contact/create/```

Authentication Required - *False*

Method Allowed - *POST*

#### Contact List

```/api/contact/list/account/<account_id>/```

Authentication Required - *True*

Method Allowed - *GET*

#### Contact Retrieve/Update/Destroy

```/api/contact/<contact_id>/```

Authentication Required - *False*

Method Allowed - *GET, PUT, PATCH, DELETE*

## Credits
Created by [Vaibhav Sharma](https://github.com/v4iv/) for [Inbound Mantra](https://www.inboundmantra.com/).