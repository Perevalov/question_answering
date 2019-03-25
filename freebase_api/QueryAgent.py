import sys
import GstoreConnector

#set the access username and password(here we only allow user with username="endpoint", password="123" to access our endpoint)
username = "endpoint"
password = "123"

#here you set your sparql query. 
sparql = "select ?s where \n" +
"{ \n" + 
" ?s  <http://www.w3.org/2000/01/rdf-schema#label>    \"footballdb ID\"@en . \n" + 
"} \n" 

# start a gStoreConnector with given IP and Port
gc = GstoreConnector.GstoreConnector("freebase.gstore-pku.com", 80)

# do query (you will get the result in json format)
print(gc.query(username, password, "freebase", sparql))
