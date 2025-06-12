# CreatifyAI
Competitor to CreatifyAI

## Project Structure

```
CreatifyAI/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
├── README.md
└── ...
```

## How to Run the Application

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/CreatifyAI.git
    cd CreatifyAI
    ```

2. **Backend Setup:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python app.py
    ```

3. **Frontend Setup:**
    ```bash
    cd frontend/creatifyAI
    npm install
    npm start dev
    ```

## Endpoints

### Backend

- `POST /api/generate` - Generate content using AI
- `GET /api/status` - Check backend status

### Frontend

- `/` - Home page
- `/dashboard` - User dashboard

## Requirements

- Python 3.8+
- Node.js 14+
- pip, npm
- All Python dependencies listed in `backend/requirements.txt`
- All Node dependencies listed in `frontend/package.json`

## GitHub

[https://github.com/sumanyunandwani/CreatifyAI](https://github.com/sumanyunandwani/CreatifyAI)
