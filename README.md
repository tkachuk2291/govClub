Вот готовый текст, который можно сразу вставлять в файл README.md:

````markdown
# Gov Club Project

## Setup

Before starting, make sure all dependencies are installed.

### FrontEnd

```bash
npm install
````

### BackEnd

```bash
pip install -r requirements.txt
```

---

## Environment Variables Setup

To run the backend correctly, create a `.env` file in the `govClubBackEnd/` directory (next to `manage.py`) and add the necessary variables.

### Example `.env` file:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
```

---

## Running the Project

### FrontEnd (port 3000)

```bash
cd govClubFrontEnd/
npm run dev
```

Open in your browser: `http://localhost:3000`

---

### BackEnd (port 8005)

```bash
cd govClubBackEnd/
python manage.py runserver 8005
```

---

## Database Migrations

The project includes a test database preconfigured for quick start.
If you want to use your own database, you **must apply migrations** to create all necessary tables (after removing the old database if it exists).

To apply migrations, run:

```bash
cd govClubBackEnd/
python manage.py migrate
```


