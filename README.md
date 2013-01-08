HouseHuntScript
===============

Parse craigslist data and filter out places based on distance from school

Thought about making this before coming to Salt Lake City. Parses craigslist feed fetching out address which then is sent
to maps API and distance is computed from the School. The shortest distance results are sent as an email. Set this up as a
job on AWS with their mailing service configured.
