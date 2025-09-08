import os
from dataclasses import asdict

import pandas as pd

from data_classes import Person
from swapi_reader import SWAPIReader
from dotenv import load_dotenv
from src.crypto_utils import JSONKeyEncryptor

# Configure pandas to show everything
pd.set_option("display.max_rows", None)     # show all rows
pd.set_option("display.max_columns", None)  # show all columns
pd.set_option("display.width", None)        # don't wrap lines
pd.set_option("display.max_colwidth", None) # don't truncate column values

if __name__ == "__main__":
    load_dotenv()
    encryptor = JSONKeyEncryptor(key=os.getenv("FERNET_KEY"))
    reader = SWAPIReader(Person, resource="people", debug=os.getenv("DEBUG") == "True")
    people = reader.fetch()
    #DECRYPTED
    # Convert list[Person] -> list[dict]
    people_dicts = [encryptor.decrypt_dict_values(asdict(p)) for p in people]
    # Create DataFrame
    df = pd.DataFrame(people_dicts)
    # Print DataFrame
    print(df.head())  # show first 5 rows


