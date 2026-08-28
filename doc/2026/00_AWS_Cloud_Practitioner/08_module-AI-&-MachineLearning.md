## AI/ML & Data Analyst :-

### AI :- 
- Artificial Intelligence is focused on building intelligent system that are capable of performing humanlike tasks.

### ML :-
- Machine learning is a type of AI for training machines to perform complex tasks without explicit instructions. 
- finding/analyzing  patterns hidden in historical data to produce an ML model.
- This ML model can then be applied to new data to make predictions/decisions based on the patterns it's learned.
- Predict trends, Make decisions, Detect anomalies, such as bank fraud.

### AWS AI/ML solutions :-
- The AWS AI/ML stack is composed of 3 tiers of solutions:
- AI Services - pre-built models, already trained that perform specific functions.
- ML Services - customized approach with Amazon SageMaker AI where you build, train, and deploy your ML models with fully managed infrastructure.
- ML Frameworks & Infrastructure - custom approach, building models using purpose-built chips that integrate with popular ML frameworks.
---

## AWS AI/ML Stack :-

## Tier 1: Pre-built AWS AI Services :
- Managed, ready-to-use models requiring no ML expertise.

## Language Services:
### 1.Amazon Comprehend: 
- Uses natural language processing,
- Extracts insights and key phrases from text.
- Content classification, customer sentiment/feedback analysis
### 2.Amazon Polly: 
- Converts text into lifelike speech.
- Supports multiple languages, different genders, and a variety of accents.
- Virtual assistants, e-learning applications
### 3.Amazon Transcribe: 
- Converts speech into text.
- Speaker identification, custom vocabulary.
- Customer call transcription, automated subtitling, and metadata generation
### 4.Amazon Translate: 
- Translates text across multiple languages.
- Real-time and batch text translation
- Document translation and multi-language application integrations

## Computer Vision & Search Services:
### 1.Amazon Kendra: 
- Intelligent search using natural language processing over enterprise data.
- Intelligent chatbots
### 2.Amazon Rekognition: 
- Analyzes images and videos for object/person,text,scenes and activity identification.
- Content moderation, identity verification, media analysis
### 3.Amazon Tex-tract: 
- Extracts text typed/handwritten and tables from documents/forms.
- Financial, healthcare, and government form text extraction for quick processing

## Conversational AI & Personalization:
### 1.Amazon Lex: 
- Builds conversational  voice and text chatbots.
- uses both Natural language Understanding (NLU) & Automatic Speech Recognition (ASR) to create lifelike conversations.
- Virtual assistants, natural language search for FAQs, and automated application bots
### 2.Amazon Personalize: 
- Delivers personalized user product and content recommendations.
- use historical data to build intelligent applications

## Tier 2: ML Services :
- Managed environments for custom model development without infrastructure overhead.

### 1.Amazon SageMaker AI: 
- Fully managed, Data scientists can use IDE to build, train, debug, and deploy custom ML models. 
- SageMaker AI to develop their ML models without worrying about infrastructure. 
- Offers low-code/no-code options alongside pre-trained models.


## Tier 3: ML Frameworks and Infrastructure :
- Complete control for expert ML teams needing maximum customization.

### 1.ML Frameworks: 
- Pre-built software libraries (e.g., PyTorch, TensorFlow, Apache MXNet).
### 2.AWS Infrastructure: 
- High-performance hardware compute resources (e.g., ML-optimized EC2 instances, EMR, ECS).

---
## Generative AI & Foundation Models :
### 1.Deep Learning
- subset of machine learning, models are trained using layers of artificial neurons that mimic the human brain.
- Each layer of these neural networks feeds information to the next layer until a final model is produced.
### 2.Generative AI
- uses pre-trained Foundation Models(FMs) to handle broad tasks like creating text, images, video, and code.
- FMs are pre-trained on vast collections of data.
- While traditional ML models are trained to perform singular tasks,
- Large language models (LLMs), are a popular type of FM trained to use human language.

---
## Generative AI on AWS :
- AWS offers the following types of generative AI solutions:
### 1.Amazon SageMaker 
- JumpStart—An ML hub with FMs and pre-built ML solutions deployable with a few clicks
### 2.Amazon Bedrock
- A fully managed service for adapting and deploying FMs from Amazon and other leading AI companies
- Enterprise-grade generative AI : Build production-ready generative AI applications with enterprise-level security, privacy, and scalability.
- Multimodal content generation : Create applications that can generate multiple content types, such as text and images.
- Advanced conversational AI : Develop advanced conversational agents that connect to your enterprise data to provide accurate responses.
### 3.Amazon Q
- integrates with your existing information repositories to answer questions, helps generate insights and new content.
- An interactive AI assistant for developers, e.g. UI of ChatGPT, Deepseek uses Bedrock.
- split into Q Business (searches enterprise data repositories) and Q Developer (generates code and automates development).
---

### SageMaker JumpStart: 
- ML hub to quickly test, fine-tune, and deploy pre-trained foundation models with minimal expertise.
- Rapid ML model deployments : Quickly deploy pre-trained models without extensive ML expertise.
- Custom fine-tuned solutions : Fine-tune pre-trained FMs with your domain-specific data.
- ML experiments and prototypes : Compare performance for different models before committing to a specific approach.

