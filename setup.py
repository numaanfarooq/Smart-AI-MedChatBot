from setuptools import find_packages, setup

setup(

    name = 'Smart AI Medical Chatbot',
    version= '0.0.0',
    author= 'Numaan Farooq',
    author_email= 'numaanfarooqds@gmail.com',
    packages= find_packages(),
    install_requires = [
       "sentence-transformers==2.2.2",
        "langchain==0.0.330",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone[grpc]",
        "langchain-pinecone",
        "langchain_community",
        "langchain_openai",
        "langchain_experimental",   
    ]
)