#!/bin/bash
# This script downloads covid data and displays ir

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalized')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests, $DEATHS deaths and $HOSPITAL hospitalized."

