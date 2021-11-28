# CN_Project
Tool to extract the names of vendors that have made ethernet/Bluetooth devices  to check the MAC fakeness.

## Steps to use the project:

1. Fork and Clone

2. Create virutal environment for the project
    ```bash
    python -m venv venv
    
    venv\Scripts\activate
    ```
3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
4. Create the database by running db_create.py

    ```bash
    python db_create.py
    ```
5. Run the app.py
    ```bash
    python app.py
    ```
 ### Also make sure that you are giving the right path to the pcap file and, also check that the file indeed is of pcap format
