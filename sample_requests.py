import argparse

from common.fixtures import first_census_entry, second_census_entry, wrong_category_entry, generate_entry
from api.requests import do_call


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Do Sample Request",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--host",
        type=str,
        help="host"
    )

    parser.add_argument(
        "--port",
        type=str,
        help="port",
        default='80'
    )


    # Add code to load in the data.
    args = parser.parse_args()
    host = args.host
    port = args.port
    do_call(host, port, first_census_entry)
    do_call(host, port, second_census_entry)
    do_call(host, port, wrong_category_entry)

    for i in range(10):
        do_call(host, port, generate_entry())