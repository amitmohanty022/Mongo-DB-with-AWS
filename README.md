# MongoDB with AWS in MongoDB Atlas

This project demonstrates a Python-based student management system using MongoDB Atlas for database operations. The project provides a command-line interface for managing student records, including admissions, certificate generation, status updates, and more.

## Features
- **Student Admission:** Add new student records to the database.
- **View Total Students:** Display all student records.
- **Course Extension:** Extend the course duration for students.
- **Placement Management:** Manage and view placed students.
- **Certificate Generation:** Verify and generate student course completion certificates.
- **Record Deletion:** Delete student records from the database.
- **Status Updation:** Update course status for students.

## Technologies Used
- **Python** (for backend logic and CLI interface)
- **MongoDB Atlas** (as the database)
- **PyMongo** (for MongoDB integration)
- **AWS Cloud Services** (for cloud storage and database hosting)

## Project Setup
1. Clone the repository:
   ```bash 
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install pymongo
   ```
3. Configure MongoDB Atlas:
   - Create a MongoDB Atlas account.
   - Set up a cluster and obtain the connection string.
4. Run the application:
   ```bash
   python main.py
   ```

## MongoDB Atlas Connection
Ensure you replace the connection string in the `MongoClient` initialization with your MongoDB Atlas URI.

```python
client = pymongo.MongoClient('mongodb+srv://<username>:<password>@cluster0.gvtwd.mongodb.net/', tlsAllowInvalidCertificates=True)
```

## Security Considerations
- Avoid hardcoding credentials in the codebase.
- Use environment variables to store sensitive information securely.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, feel free to reach out via [GitHub Issues](https://github.com/yourusername/mongodb-aws/issues).

