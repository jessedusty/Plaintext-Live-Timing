# Simple Live Timing Race Results View

This flask server parses alpine skiing results from live-timing.com and returns them in a plain-text list.

The server can list all racers and places from a particular race, or filter by team by changing the URL parameter. 

# Modes

## Show all for a race

`http://<server>:8080/scores/<race_id>` where race_id is the race number from live-timing's URL

## Filter race results for one team

`http://<server>:8080/teams/<team>/<race_id>` where team is the short-id of the team listed on the results page. e.g. "SIT" for Stevens Institute of Technology

# Pebble Integration

To show results on a Pebble smartwatch use this pebble app: https://github.com/bahbka/pebble-my-data

Configure the URL in the settings screen to point to these URLS:
`http://<server>/p/scores/<race_id>` for race filtering
`http;//<server>/p/teams/<team>/<race_id>` for team filtering
