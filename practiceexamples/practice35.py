#program to get variable unique identification number or string.
"""A unique identifier is a string or number used to identify a resource (such as an object, file, or database record) in a unique and consistent way. 
  A unique identifier can be generated in several ways, including:

    UUID (Universally Unique Identifier): A 128-bit identifier that is generated randomly to ensure uniqueness.

    GUID (Globally Unique Identifier): A 128-bit identifier that is used to identify resources across multiple systems or networks.

    Timestamp-based identifier: A unique identifier that is generated based on the current time, such as a Unix timestamp.

    Auto-incrementing identifier: A unique identifier that is generated based on an incrementing counter, such as a primary key in a database table.
"""
import uuid
def unique_id():
    unique_id=str(uuid.uuid1())
    print(unique_id)

unique_id()


