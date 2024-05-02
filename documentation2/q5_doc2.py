# Q.4: The Python documentation for the datetime module provides two attributes to retrieve the year from a
# date or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# What is the difference between the year attribute and the isocalendar method?

# The year attribute represents a range between 1 - 9999 in years. Attribute of a date or datetime object simply returns
# the year of that date.

# Return a named tuple object with three components: year, week and weekday.
#
# The ISO calendar is a widely used variant of the Gregorian calendar. [3]
# The ISO year consists of 52 or 53 full weeks, and where a week starts on a Monday and ends on a Sunday.
# The first week of an ISO year is the first (Gregorian) calendar week of a year containing a Thursday.
# This is called week number 1, and the ISO year of that Thursday is the same as its Gregorian year.

