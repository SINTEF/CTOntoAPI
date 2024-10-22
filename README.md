# CTOntoAPI

CTOntoAPI is an API designed to facilitate the interaction with the [CircularTwAIn Ontology Library](https://github.com/Circular-TwAIn/CircularTwAIn-Ontology-Library). This API provides various endpoints to query the data efficiently based on input string.

## Features

The backend provides API to:
- Query the ontology classes and properties based on string input.
- Retrive labels, data properties, object property of a node.
- Query the ontology with SPARQL query.
- Integration with the LamAPI for query Wikidata Knowledge Graph

The Frontend provide vizualization of the ontology and the query results.

## Usage

### Run with Docker

To run the API server with Docker, run:

```bash
docker-compose up
```

### Run with Python
GraphDB is required to run the API. The GraphDB image built with the ontologies is available at the [CircularTwAIn Packages](https://github.com/orgs/Circular-TwAIn/packages). To start it, run:

```bash
docker run -d -p 7200:7200 ghcr.io/circular-twain/ctontolib/graphdb-image:latest
```
Then run the backend and frontend with:

```bash
python run_backend.py
python run_frontend.py
```

You might need to install the required packages with:

```bash

pip install -r ./backend/requirements.txt
pip install -r ./frontend/requirements.txt
```

## Endpoints
The backend is available at `http://localhost:9001` and the frontend is available at `http://localhost:9002`.
You can change the port in the [environment and configuration folder](./environment_and_configuration).



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact me at [An Lam](mailto:an.lam@sintef.no).
