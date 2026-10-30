# MongoDB with AWS (MongoDB Atlas)

A command-line student management system in Python. It stores data in a **MongoDB Atlas** cluster hosted on AWS.

## Features
- **Student Admission:** add new student records.
- **View Total Students:** list all students.
- **Course Extension:** extend a student's course duration.
- **Placement Management:** add and list placed students.
- **Certificate Check:** show the record if the course is completed.
- **Record Deletion:** delete a student record.
- **Status Update:** change a student's course status (for example to `Completed`).

## How to run (step by step)

You need **Python 3.10 or newer** ([download](https://www.python.org/downloads/)) and a free **MongoDB Atlas** account.

**1. Download the project**

```bash
git clone https://github.com/amitmohanty022/Mongo-DB-with-AWS.git
cd Mongo-DB-with-AWS
```

**2. Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

**3. Install the requirements**

```bash
pip install -r requirements.txt
```

**4. Get your MongoDB Atlas connection string**

1. Sign in at https://cloud.mongodb.com and create a free cluster. Choose **AWS** as the provider.
2. Under **Database Access**, add a database user with a username and password.
3. Under **Network Access**, add your IP address, or `0.0.0.0/0` for testing.
4. Click **Connect → Drivers → Python** and copy the connection string. It looks like:
   `mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/`

**5. Put the connection string in `.env`**

- Copy `.env.example` to a new file named `.env`
  - Windows: `copy .env.example .env`
  - macOS / Linux: `cp .env.example .env`
- Open `.env` and paste the string after `MONGODB_URI=`, with your real username and password filled in.

**6. Start the app**

```bash
python ducat.py
```

**7. Use it**

Type a number from the menu and press Enter:

```
1 New Admission        4 Add Placed Student     7 Update Status
2 Total Students       5 Certificate of Course  8 Placed Student List
3 Course Extension     6 Delete a Record        9 Exit
```

The app uses the database `Ducat`, with the collections `students` and `placed`. They are created automatically on first insert.

## Security
- The connection string is read from `.env`, which git ignores. Never commit it.
- TLS certificates are verified using `certifi`.

## Troubleshooting

| Problem | Fix |
|---|---|
| "MONGODB_URI is not set" | Make sure the file is named exactly `.env` and is in the project folder. |
| `ServerSelectionTimeoutError` | Add your IP address under **Network Access** in Atlas. |
| `bad auth : authentication failed` | Check the username and password in the URI. Special characters in the password must be URL-encoded (for example `@` → `%40`). |

## License
MIT
