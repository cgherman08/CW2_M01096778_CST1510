# Operational Intelligence Hub

**CST1510 Module Coursework**

A multi-page Streamlit application for managing cybersecurity incidents, IT tickets, datasets, and AI-assisted operations intelligence.

---

## 🏗️ Architecture Overview

### **Project Structure**

```
CW2_M01096778_CST1510/
├── Home.py                    # Main landing page with navigation
├── pages/                     # Multi-page app sections
│   ├── 1_🔐 _Login.py        # Authentication and account management
│   ├── 2_🛡️ _Cybersecurity.py # Security incident dashboard with charts
│   ├── 3_📊 _Data_Science.py  # Dataset catalog viewer
│   ├── 4_💻 _IT_Operations.py # IT ticket management and analytics
│   └── 5_🤖 _AI_Assistant.py  # AI chat powered by Groq API
├── services/                  # Business logic layer
│   ├── auth_manager.py        # Authentication and password hashing
│   ├── database_manager.py    # SQLite queries and data migration
│   └── ai_assistant.py        # AI model integration helpers
├── models/                    # Data model classes
│   ├── user.py
│   ├── security_incident.py
│   ├── it_ticket.py
│   └── dataset.py
├── database/                  # SQLite database storage
│   └── intelligence_platform.db
├── DATA/                      # Seed data (CSV files)
│   ├── cyber_incidents.csv
│   ├── it_tickets.csv
│   ├── datasets_metadata.csv
│   └── users.txt
└── app/                       # Legacy modules (deprecated)
```

### **Technology Stack**

- **Frontend**: Streamlit (multi-page app with session state)
- **Backend**: Python 3.9+
- **Database**: SQLite3
- **Charting**: Altair (declarative visualizations)
- **Authentication**: bcrypt password hashing
- **AI Integration**: Groq API (free tier with GPT models)

### **Key Features**

1. **Session-based Authentication**: Login/logout with bcrypt-hashed passwords
2. **Role-agnostic Access**: All authenticated users see the same dashboards
3. **Real-time Filtering**: Multi-select filters on incidents and tickets
4. **Interactive Charts**: Bar charts, line charts, and timelines using Altair
5. **AI Chat Assistant**: Context-aware conversational AI powered by Groq
6. **Account Management**: Update username or delete account with confirmation

---

## 🚀 Setup Instructions

### **1. Prerequisites**

- Python 3.9 or higher
- pip (Python package manager)

### **2. Clone the Repository**

```bash
cd CW2_M01096778_CST1510
```

### **3. Install Dependencies**

```bash
pip install -r Requiremens.txt
```

**Required packages:**
- `streamlit` - Web application framework
- `pandas` - Data manipulation
- `altair` - Chart rendering
- `bcrypt` - Password hashing
- `groq` - AI model API client

### **4. Initialize the Database**

Run the data migration script to populate SQLite from CSV files:
Make sure to change the path from database_manager.py from DBMigrator class to specify the file you want to migrate.
```bash
python -c "from services.database_manager import DBMigrator; m=DBMigrator(); m.migrate_cyber_incidents(); m.migrate_it_tickets(); m.migrate_datasets_metadata(); m.migrate_users(); print('Database initialized')"
```

This creates `database/intelligence_platform.db` with all tables populated.

---

## ▶️ Running the Application

### **Start the Streamlit Server**

```bash
streamlit run Home.py
```

The app will open in your default browser at `http://localhost:8501`.

### **First-Time Login**

Click **Register** to create a new account.

---

## 📂 Page Descriptions

### **Home**
- Landing page with navigation buttons
- Quick access to Login/Register
- Module overview

### **Login (🔐)**
- Two-tab interface: Log In / Register
- Account management section when logged in:
  - Change username
  - Delete account (with confirmation)
  - Log out

### **Cybersecurity (🛡️)**
- Displays cyber incidents from the database
- Multi-select filters: Severity, Status, Date Range
- Charts:
  - Incidents by status (bar chart)
  - Incidents by severity (bar chart)
  - Incidents by category (bar chart)
  - Daily timeline (line chart)
- Sortable data table with full incident details

### **Data Science (📊)**
- Dataset catalog viewer
- Shows metadata: name, rows, columns, uploaded_by, upload_date
- Interactive table with search and sort

### **IT Operations (💻)**
- IT ticket dashboard with filters: Priority, Status, Assignee
- Charts:
  - Tickets by priority (bar chart)
  - Tickets by status (bar chart)
  - Tickets by assignee (bar chart)
  - Weekly ticket volume (line chart)
- Sortable ticket table

### **AI Assistant (🤖)**
- Chat interface powered by Groq API
- Model selection: OpenAI GPT-OSS-120B or others
- Free API key required (get at https://console.groq.com)
- Context-aware responses about incidents, tickets, and datasets

---

## 🔒 Security Notes

- Passwords are hashed with bcrypt before storage
- Session state manages authentication (not persistent across browser sessions)
- SQLite database is local and not encrypted
- AI API keys are session-only and not stored

---

## 🐛 Troubleshooting

### **No data showing on dashboards**
- Ensure you've run the database migration script (see Setup step 4)
- Check that `database/intelligence_platform.db` exists
- Verify you're logged in (pages redirect to Login if not authenticated)

### **AI Assistant not responding**
- Ensure you've entered a valid Groq API key in the sidebar
- Check internet connection (API is cloud-hosted)
- Free tier may have rate limits

### **"Module not found" errors**
- Reinstall dependencies: `pip install -r Requiremens.txt`
- Ensure you're running from the project root directory

---

## 📝 Future Enhancements

- [ ] Persistent sessions with cookies
- [ ] Role-based access control (admin vs. user)
- [ ] Export charts as PNG/CSV
- [ ] Real-time incident notifications
- [ ] Integration with external ticketing systems

---

## 👤 Author

**Student Name**: Catalin Gherman
**Module**: CST1510  
**Institution**: Middlesex University

---

## 📄 License

This project is submitted as coursework for academic evaluation. All rights reserved.
