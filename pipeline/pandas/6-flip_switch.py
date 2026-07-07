#!/usr/bin/env python3
"""Sort a DataFrame in reverse chronological"""


def flip_switch(df):
    """Flips based on Timestamp"""

    return df.sort_values('Timestamp', ascending=False)
