#!/usr/bin/env python3
"""
    Create and populate master tables in Postgres (if they don't exist).

    Database: retrosheet
    Tables:
        1) Team detail master (year by year)
        2) Player detail master (Source: https://www.retrosheet.org/BIOFILE.TXT)
        3) Team rosters (year by year)
        4) Game event details
        5) Ballpark details (Source: https://www.retrosheet.org/parkcode.txt)
"""

import sys
import os

import db
import schema


if __name__ == "__main__":
    # Connection establishment
    argv = sys.argv[1:]
    try:
        conn = db.get_connection(argv)
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # Table creation
    try:
        db.execute_single_query(conn, schema.team_detail_master)
        db.execute_single_query(conn, schema.player_detail_master)
        db.execute_single_query(conn, schema.team_roster_master)
        db.execute_single_query(conn, schema.game_event_detail_master)
        db.execute_single_query(conn, schema.ballpark_detail_master)
    except Exception as e:
        print(str(e))
        sys.exit(2)

    conn.commit()
    conn.close()
