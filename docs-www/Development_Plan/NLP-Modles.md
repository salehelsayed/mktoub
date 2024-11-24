# NLP Models Overview

## Model Architecture

```mermaid
graph TB
    User[User Input] --> Preprocessing[Text Preprocessing]
    Preprocessing --> Intent[Intent Recognition]
    Preprocessing --> Entity[Entity Recognition]
    
    subgraph "Intent Recognition"
        Intent --> BERT[BERT Model]
        Intent --> Rasa[Rasa Classifier]
        BERT --> IntentOutput[Intent Classification]
        Rasa --> IntentOutput
    end
    
    subgraph "Entity Recognition"
        Entity --> SpaCy[SpaCy NER]
        Entity --> HuggingFace[BERT-base-NER]
        SpaCy --> EntityOutput[Named Entities]
        HuggingFace --> EntityOutput
    end
    
    IntentOutput --> TaskProcessor[Task Processor]
    EntityOutput --> TaskProcessor
    TaskProcessor --> Database[(SQLite Database)]
    TaskProcessor --> Response[Response Generator]
```

## Model Details

### Text Preprocessing
- Tokenization
- Normalization
- Stop word removal
- Lemmatization

### Intent Recognition Models
1. **BERT Model**
   - Fine-tuned for task classification
   - Handles complex queries
   - Local processing capability

2. **Rasa Classifier**
   - Specialized for intent detection
   - Pattern matching
   - Rule-based classification

### Entity Recognition Models
1. **SpaCy NER**
   - Lightweight and fast
   - Pre-trained on general entities
   - Custom entity training support

2. **BERT-base-NER**
   - Deep learning based
   - Higher accuracy for complex entities
   - Transfer learning capability

### Task Processing
```mermaid
sequenceDiagram
    participant U as User
    participant P as Preprocessor
    participant I as Intent Classifier
    participant E as Entity Extractor
    participant T as Task Processor
    participant D as Database

    U->>P: Input Text
    P->>I: Processed Text
    P->>E: Processed Text
    I->>T: Intent Classification
    E->>T: Extracted Entities
    T->>D: Store Task Data
    D-->>T: Confirmation
    T-->>U: Response
```

### Database Schema
```mermaid
erDiagram
    TASKS {
        int task_id PK
        string description
        datetime created_at
        datetime deadline
        string status
        string priority
    }
    
    ENTITIES {
        int entity_id PK
        int task_id FK
        string entity_type
        string entity_value
    }
    
    INTENTS {
        int intent_id PK
        int task_id FK
        string intent_type
        float confidence
    }
    
    TASKS ||--o{ ENTITIES : contains
    TASKS ||--o{ INTENTS : has
```
```mermaid
flowchart LR
    A[User Input] --> B[Intent Recognition]
    B --> C[Entity Recognition]
    C --> D[Task Processing (CRUD Operations)]
    D --> E[Generate Response]
    E --> F[User Output]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#f96,stroke:#333,stroke-width:2px
```
