# pxGridRESTXapp

pxGridRESTXapp is a Flask-RESTX based API application that serves as an external REST API to provide JSON data for endpoint attributes in conjunction with Cisco pxGrid Direct for Cisco Identity Services Engine (ISE). It pulls the data from a CSV file named `pxgrid_direct.csv`, which serves as an alternative way to test the CMDB (Configuration Management Database) integration with pxGrid Direct.

## Background Information

Cisco pxGrid Direct is a feature that allows Cisco ISE to connect to external REST APIs like pxGridRESTXapp to fetch JSON data for endpoint attributes. This process facilitates the rapid evaluation and authorization of endpoints by importing the data directly into the ISE database, thereby avoiding redundant queries during the authorization process.

When using pxGrid Direct, two mandatory fields, the Unique Identifier and the Correlation Identifier, are critical for accurate data retrieval and correlation between the API and the ISE database. If a connector lacks values for these identifiers, it may lead to errors in data fetching and saving. pxGridRESTXapp is tailored to meet these requirements, ensuring seamless integration with Cisco pxGrid Direct.

## Use Case Description

pxGridRESTXapp enables users to query and filter endpoint attribute data, providing a convenient method for accessing all items or only those that have been recently updated. This capability is especially valuable for network monitoring and analytics, as it allows for the integration of endpoint data into authorization policies and other workflows within Cisco ISE.

![Demo of pxGridRESTXapp](img/pxGridRESTXapp.gif)

## Installation

To install and run the pxGridRESTXapp:

1. Clone the repository:

   ```
   git clone https://github.com/pamosima/pxGridRESTXapp.git
   ```

2. Navigate to the repository directory:

   ```
   cd pxGridRESTXapp
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```
   source venv/bin/activate
   ```

5. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Modify parameters in RESTX_app.py:
   By default, the application runs on `127.0.0.1:5000`. If you need to run the application on a different IP address or port, adjust the `app.run()` call in the `app.py` file with the desired host and port:

   ```
   app.run(host='desired_host_ip', port=desired_port, debug=True)
   ```

   Replace `desired_host_ip` with your machine's IP address or `0.0.0.0` to listen on all interfaces, and `desired_port` with the port number you wish to use.

7. Run the application:

   ```
   python RESTX_app.py
   ```

## Usage

Before making API calls, modify the `pxgrid_direct.csv` file with the corresponding endpoint information to reflect the data that you intend to provide to Cisco ISE.

After starting the application, the API endpoint available is:

- `/endpoints`: Returns all items from the CSV file by default. It accepts optional query parameters, `limit` (number of items to return) and `hours` (time frame in hours to filter updated items), to return items that have been updated within the specified time frame.

For example, to get the latest 10 items updated within the last 2 hours, the API call would look like this:

```
http://<host>:<port>/endpoints?limit=10&hours=2
```

Configure ISE pxGrid Direct based on the steps provided in the Cisco guide. Detailed instructions can be found at: [Configure and Troubleshoot ISE 3.3 pxGrid Direct](https://www.cisco.com/c/en/us/support/docs/security/identity-services-engine-33/221004-configure-and-troubleshoot-ise-3-3-pxgri.html)

## API Documentation

Swagger documentation is automatically generated and can be accessed at:

```
http://<host>:<port>/swagger/
```

This documentation provides detailed information about the API endpoint, including the query parameters, and allows for easy testing of the API directly from the interface.

## Known Issues

Currently, there are no known issues. Should you encounter any bugs or problems, please report them using the GitHub Issues section.

## Getting Help

If you encounter any issues or require assistance, please raise an issue in the GitHub repository for support.

## Getting Involved

Contributions to the pxGridRESTXapp project are welcome. Please refer to the [CONTRIBUTING](./CONTRIBUTING.md) guide for instructions on how to make contributions.

## Author(s)

This project was written and is maintained by the following individual(s):

- Patrick Mosimann <pamosima@cisco.com>
