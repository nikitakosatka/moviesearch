# MovieSearch

Flask REST API with Movies & Directors

## Setup

1. Create PostgreSQL DB
2. Create .env file in root of project & fill like in .env.example
3. Use Virtual Environment `source venv/bin/activate`
3. Install requirements `pip install -r requirements.txt`
   or `pip3 install -r requirements.txt`
4. Run application `flask run -h 127.0.0.1 -p 8080`

## Custom Exceptions

*RatingValidationException*

*YearValidationException*

## Unit Test

*test_get_directors()*
*test_get_movies()*

## Provided Endpoints

### Movie endpoints

1. GET /api/movies. 200 OK example

```json
{
  "list": [
    {
      "id": 1,
      "title": "Example movie",
      "year": 2018,
      "director": 1,
      "length": "02:30:00",
      "rating": 8
    }
  ]
}
```

2. GET /api/movies/:id. 200 OK example

```json
{
  "movie": {
    "id": 1,
    "title": "Example movie",
    "year": 2018,
    "director": 1,
    "length": "02:30:00",
    "rating": 8
  }
}
```

3. POST /api/movies. Body Example

```json
{
  "movie": {
    "title": "Example movie",
    "year": 2018,
    "director": 1,
    "length": "02:30:00",
    "rating": 8
  }
}
```

Response

```json
{
  "movie": {
    "id": 1,
    "title": "Example movie",
    "year": 2018,
    "director": 1,
    "length": "02:30:00",
    "rating": 8
  }
}
```

4. PATCH /api/movies. Body Example

```json
{
  "movie": {
    "title": "Example movie",
    "year": 2018,
    "director": 1,
    "length": "02:30:00",
    "rating": 8
  }
}
```

Response

```json
{
  "movie": {
    "id": 1,
    "title": "Example movie",
    "year": 2018,
    "director": 1,
    "length": "02:30:00",
    "rating": 8
  }
}
```

### Director endpoints

1. POST /api/directors. 200 OK example

```json
{
  "list": [
    {
      "id": 1,
      "fio": "Ivanov Ivan Ivanovich"
    }
  ]
}
```

2. GET /api/directors/:id. 200 OK example

```json
{
  "director": {
    "id": 1,
    "fio": "Ivanov Ivan Ivanovich"
  }
}
```

3. POST /api/directors. Body Example

```json
{
  "director": {
    "id": 1,
    "fio": "Ivanov Ivan Ivanovich"
  }
}
```

Response 201 OK

```json
{
  "director": {
    "id": 1,
    "fio": "Ivanov Ivan Ivanovich"
  }
}
```

4. PATCH /api/directors. Body Example

```json
{
  "director": {
    "id": 1,
    "fio": "Ivanov Ivan Ivanovich"
  }
}
```

Response 201 OK

```json
{
  "director": {
    "id": 1,
    "fio": "Ivanov Ivan Ivanovich"
  }
}
```


