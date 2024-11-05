# Embrapa Data API

## Introdution
API created to return data relating to Embrapa winemaking.

## Dependencies
Install all dependencies:
```
pip install -r requirements.txt
```

## Usage (Local)
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
- {option}: *"viniferas" | "americanas_e_hibridas" | "uvas_de_mesa" | "sem_classificacao"*
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
- {option}: *"vinhos_de_mesa" | "espumantes" | "uvas_frescas" | "uvas_passa" | "suco_de_uva"*
- **GET**

### Exportation
Endpoint used to return grape derivatives export data.

- /exportation?year={year}&option={option}
- {year}: *string*
- {option}: *"vinhos_de_mesa" | "espumantes" | "uvas_frescas" | "uvas_passa" | "suco_de_uva"*
- **GET**

# Production
You can access api in:
```
embrapa-web-scraping-api-tc.vercel.app\
```
You can access Swagger in:
```
embrapa-web-scraping-api-tc.vercel.app\docs
```

# Usage (production)
You can access api in:
```
embrapa-web-scraping-api-tc.vercel.app\
```
You can access Swagger in:
```
embrapa-web-scraping-api-tc.vercel.app\docs
```



