# PROJECT DOCUMENTATION

## Set-up Instructions

1. Clone GitHub project and Install Python

2. Install Requirements File:
    ```
    pip install -r requirements.txt
    ```

3. Enter Project directory:
    ```
    cd stage_two
    ```

4. Run development server:
    ```
    python manage.py runserver
    ```

<br>

## API Usage
Navigate to `127.0.0.1:8000` in your browser, and you should see a user-friendly interface for making requests to the API

<br>

## API ENDPOINTS

### `1. /api`

ALLOWED METHODS: `POST (CREATE)`

Request Body Format:

```json
{
    "name": "Delight"
}
```

Response Body Format:
```json
{
    "id": 1,
    "name": "Delight"
}
```

### `2. /api/user_id`

ALLOWED METHODS: `GET PUT (UPDATE) DELETE`

`GET` :

Response Body Format:
```json
{
    "id": 1,
    "name": "Delight"
}
```

`PUT (UPDATE)` :

Request Body Format:
```json
{
    "name": "Delight"
}
```

Response Body Format:
```json
{
    "id": 1,
    "name": "Delight"
}
```

`DELETE` :

Request Body Format:
```json
{
    "name": "Delight"
}
```

Response Body Format:

```
Status code: 204
```

### NOTE: `user_id` can be `name` or `id`

