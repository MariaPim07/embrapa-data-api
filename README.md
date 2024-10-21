# Embrapa Data API

## Introdution
API created to return data relating to Embrapa winemaking.

## Dependencies
FastAPI
```
pip install "fastapi[standard]"
```
Requests
```
pip install requests
```
BeautifulSoup
```
pip install
```

## Usage
Access to clone repository:
```
https://github.com/MariaPim07/embrapa-data-api/tree/master
```
To run this app:
```
fastapi run main.py
```
You can access api in:
```
http://localhost:8000
```
You can access Swagger in:
```
http://localhost:8000/docs
```

## Endpoints
### Production
Endpoint used to return wine production data,
juices and derivatives from Rio Grande do Sul

- /production?year={year}
- {year}: *string*
- **GET**

### Processing
Endpoint used to return data from
quantity of grapes processed in Rio Grande do Sul.

- /processing?year={year}&option={option}
- {year}: *string*
- {option}: *Option (string)*
- **GET**

### Commercialization
Endpoint used to return data from
marketing of wines and derivatives in Rio Grande do Sul.

- /commercialization?year={year}
- {year}: *string*
- **GET**

### Importation
Endpoint used to return grape derivatives import data.

- /importation?year={year}&option={option}
- {year}: *string*
- {option}: *Option (string)*
- **GET**

### Exportation
Endpoint used to return grape derivatives export data.

- /exportation?year={year}&option={option_ex}
- {year}: *string*
- {option_ex}: *Option_Ex (string)*
- **GET**

#### Option
- "subopcao=subopt_01"
- "subopcao=subopt_02"
- "subopcao=subopt_03"
- "subopcao=subopt_04"

#### Option_Ex
- "subopcao=subopt_01"
- "subopcao=subopt_02"
- "subopcao=subopt_03"
- "subopcao=subopt_04"
- "subopcao=subopt_05"



