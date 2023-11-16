from smbprotocol.connection import Connection, Dialects
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
import socket
import traceback
import uuid

def check_smb_signing(ip_address, port=445):
    try:
        # Establish a socket connection
        connection = Connection(uuid.uuid4(), '172.16.16.172', 445)
        connection.connect(Dialects.SMB_3_1_1)
        # Create a session
        session = Session(connection, username='Shakthivel', password='iAmShakthi')
        session.connect()
        # Check the signing requirements
        signing_required = session.signing_required
        print(f"SMB Signing Required: {signing_required}")
    except Exception:
        print(traceback.format_exc())

check_smb_signing('10.200.10.9')