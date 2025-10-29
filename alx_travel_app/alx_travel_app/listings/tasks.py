import logging
from datetime import datetime
from celery import shared_task
from gql import gql, Client
from gql.transport import requests
from gql.transport.requests import RequestsHTTPTransport
