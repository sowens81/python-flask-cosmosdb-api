from pymongo import MongoClient

client = MongoClient('mongodb://sopythondev:v9mJl9aHuotgiS0xHldSgRUaWCEASTv1Jbn82SkQqfRiEEj6XcnXBacvMoV1JU7GretigdcfkRdqZwpECSSjbg==@sopythondev.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')

db = client.flask_users

