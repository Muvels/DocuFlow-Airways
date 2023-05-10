# DocuFlow [Airways]

DocuFlow is a key-value extractor developed with LSH and AI.
The Task of Docuflow is to read Pdf Documents and to find specific Values that are needed to create a Order from an MAWB/HAWB Manifest

## How it works:

First, the User sends an Http GET request to an running Flask Server, here the Document gets submitted with MIME-Type Multipart-Form Data

Second, the AI scans the submittet Manifest and find Boxes where the Value for a specific Key is usually in it. Coordinates will be returned.

Third, the Text in the Boxes the AI found will be extracted and given to the [LSHEngine Library](https://github.com/Muvels/LSHEngine), here the text gets compared to Thousands of other Data to detect Similarity in order to find a fitting key to each value. The compared values with the greatest overlap (measured by the Jaquard Value) are summarised as a key value pair.

After that the key value Pairs will be converted to JSON format and returned from the flask Server to the User.

## Example Input:

You can see an Expamle Input File in the network_client/pdfs directory

## Example Output:

You can see an Expamle Output File in the network_client/output directory





