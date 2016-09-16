"""Functions used by the default implementation of the Stash class."""

def make_date_prefix(date):
    """Make an S3 key prefix from a date.

    Format a date as:

        YYYY/MM-Month/DD/

    For example:

        2016/09-September/15/

    """
    return date.strftime('%Y/%m-%B/%d/')
