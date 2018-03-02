from pycricbuzz import Cricbuzz
import json
c = Cricbuzz()
matches = c.matches()
for match in matches:
    print (json.dumps(c.scorecard(match['id']),indent=4))
    break
