"""
OpenTable Reviews API: A Quick Start Example
See more at: https://apify.com/johnvc/opentable-reviews-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/opentable-reviews-api/input-schema?fpr=9n7kx3

This script shows how to call the OpenTable Reviews API on Apify from Python and
read its structured JSON output. It pulls a restaurant's reviews with the full
rating breakdown. Inputs are kept small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one restaurant, 10 reviews) to keep this first run
# inexpensive: you are billed per review returned. The restaurant ID is the
# OpenTable URL slug (the "r/..." path).
run_input = {
    "restaurantId": "r/central-park-boathouse-new-york-2",
    "maxResultsPerRestaurant": 10,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/opentable-reviews-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} row(s).\n")

# Show each review with its rating and text.
for item in items:
    if item.get("result_type") != "review":
        continue
    rating = (item.get("rating") or {}).get("overall")
    diner = (item.get("user") or {}).get("name", "")
    content = item.get("content", "")
    print(f"{item.get('position')}. {diner} rated {rating}/5")
    print(f"   {content[:160]}\n")
