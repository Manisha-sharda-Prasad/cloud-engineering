flowchart LR
A["👤 Client<br/>Browser / Mobile App"]

    B["🌐 DNS<br/>Domain → IP"]

    C["🚪 API Gateway<br/>Authentication / Routing"]

    D["⚖️ Load Balancer<br/>Distributes Traffic"]

    E1["🖥️ Server Node 1<br/>Application"]
    E2["🖥️ Server Node 2<br/>Application"]
    E3["🖥️ Server Node 3<br/>Application"]

    F["⚙️ Business Logic<br/>Service Layer"]

    G["🗄️ Database<br/>Data Storage"]

    H["⚡ Cache<br/>Redis / Memcached"]

    I["📦 External Service<br/>Payment / Email / API"]

    A -->|"1. HTTPS Request"| B
    B -->|"2. Resolve Domain"| C
    C -->|"3. Forward Request"| D

    D -->|"4. Route"| E1
    D -->|"4. Route"| E2
    D -->|"4. Route"| E3

    E1 --> F
    E2 --> F
    E3 --> F

    F -->|"Read / Write"| G
    F -->|"Fast Data Access"| H
    F -->|"API Call"| I

    G -->|"Data"| F
    H -->|"Cached Data"| F
    I -->|"Response"| F

    F --> E1
    F --> E2
    F --> E3

    E1 -->|"HTTP Response"| D
    E2 -->|"HTTP Response"| D
    E3 -->|"HTTP Response"| D

    D --> C
    C --> A

