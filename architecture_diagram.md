graph TB
    subgraph "Frontend Layer"
        FE[React Frontend<br/>localhost:3000]
    end
    
    subgraph "Backend Layer"
        API[FastAPI Server<br/>localhost:8000]
        PARSER[Parser Service<br/>BeautifulSoup4]
        BOT[Telegram Bot Service]
    end
    
    subgraph "Data Layer"
        DB[(PostgreSQL<br/>medbook_db)]
        CACHE[(Redis Cache<br/>опционально)]
    end
    
    subgraph "External Services"
        TG[Telegram API]
        WEB[Websites for Parsing]
    end
    
    FE --> API
    API --> DB
    API --> PARSER
    PARSER --> WEB
    BOT --> API
    BOT --> TG
    API -.-> CACHE
    
    style FE fill:#e1f5fe
    style API fill:#f3e5f5
    style DB fill:#e8f5e8
    style PARSER fill:#fff3e0
    style BOT fill:#fce4ec