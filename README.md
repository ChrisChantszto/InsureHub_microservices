# Policy PDF Microservice

This microservice accepts JSON data representing policy details, and returns a PDF file of the policy.

**NOTE:** The `policyData` object provided in these examples is assumed to be queried from a MongoDB database. The examples here do not include the MongoDB connection and query code. You will need to implement those parts yourself based on your specific database schema and setup.

## Requesting Data

To request data from this microservice, you need to send a POST request to the `/export-to-pdf` endpoint. The body of the request should be a JSON string representing the policy details.

An example request using `fetch` in JavaScript might look like this:

```javascript
// TODO: Replace this with your actual code to query data from MongoDB
var policyData = {
    "policyNumber": "12345",
    "policyProvider": "Provider Inc.",
    "policyType": "Type A",
    "startDate": "2023-01-01",
    "endDate": "2023-12-31",
    "premium": 1000,
    "paymentDate": "2023-01-15"
};

fetch('http://localhost:5000/export-to-pdf', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(policyData)
}).then(function(response) {
    // handle response
});
```

## Receiving Data

After making a POST request to the /export-to-pdf endpoint, the server will return a PDF file. You can programmatically receive this file using the Response.blob() method in the Fetch API.

An example of this might look like the following:

```javascript
fetch('http://localhost:5000/export-to-pdf', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(policyData)
}).then(function(response) {
    return response.blob();
}).then(function(blob) {
    // handle PDF blob
});
```

This will return a blob object representing the PDF file. You can then use this object to create a blob URL and display the PDF in the browser, or download the PDF to the users computer.

## UML Sequence Diagram

Please see the included UML sequence diagram for a detailed flow of how requesting and receiving data works in this microservice.

The UML diagram shows the process of a client making a request to the server, the server processing the request and returning a PDF file, and the client receiving the PDF file. The process includes error handling and logging. (Note: You'll need to create an actual UML sequence diagram and include it in your repository, replacing ./uml-sequence-diagram.png with the actual path to your diagram.)---Please ensure your requests adhere to the format outlined in this document. If you have any problems or questions, don't hesitate to reach out.**NOTE:** Markdown doesn't support nested code blocks, so you'll need to remove the outermost set of triple backticks () before using this in a README file. Also, make sure to replace ./uml-sequence-diagram.png with the actual path to your UML sequence diagram.
