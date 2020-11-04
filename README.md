mocketoy
========

Client-Server Toy initially designed for our talk at Europython 2013

- Morpheus is your real server, that's exactly what we want to mock;
- Neo is your client, basically what we want to test.

Mocket shows its power in the tests file, where you can see the first test using the real server, and a couple of tests using *mocketize* decorator.

Quick Start

```sh
# Install Dependencies to a local .venv/
python -m pip install -r requirements.txt

# In separate shells, run the server and the client:
python morpheus.py
python neo.py

# One test expects the server (morpheus.py) to be running, while the other two tests demonstrate mocking
python morpheus.py
python -m unittest tests.py
```
