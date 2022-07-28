"""
    Schema strings for table creation/manipulation.
    Subject to change over time, so centralizing for now.
"""

import os

team_detail_master = """CREATE TABLE IF NOT EXISTS team_detail_master (
                            year SMALLINT,
                            team CHAR(3),
                            league_key CHAR(1),
                            city TEXT NOT NULL,
                            nickname TEXT NOT NULL,
                            PRIMARY KEY (year, team)
                        );"""

player_detail_master = """CREATE TABLE IF NOT EXISTS player_detail_master (
                            player_id CHAR(8) PRIMARY KEY,
                            last_name TEXT NOT NULL,
                            first_name TEXT NOT NULL,
                            nickname TEXT,
                            birthdate DATE,
                            debut_date DATE,
                            last_game_date DATE
                        );"""

team_roster_master = """CREATE TABLE IF NOT EXISTS team_roster_master (
                            year SMALLINT,
                            team CHAR(3),
                            player_id CHAR(8),
                            PRIMARY KEY(year, team, player_id)
                        );"""

ballpark_detail_master = """CREATE TABLE IF NOT EXISTS ballpark_detail_master (
                                park_id CHAR(5) PRIMARY KEY,
                                name TEXT NOT NULL,
                                nickname TEXT,
                                city TEXT,
                                state CHAR(2),
                                start_date DATE,
                                end_date DATE,
                                league CHAR(2)
                            );"""

"""
    Game event detail table creation.
    Query + data structures to programmatically make the cwevent call based on query structure (in case of change).
    
    Source: https://chadwick.readthedocs.io/en/latest/cwevent.html#cwtools-cwevent-eventtype
"""

game_event_detail_master_fields = open(f'{os.path.dirname(__file__)}/.dict/game_event_detail_master_fields.dict')

game_event_detail_optional_fields = open(f'{os.path.dirname(__file__)}/.dict/game_event_detail_optional_fields.dict')

game_event_detail_master = """CREATE TABLE IF NOT EXISTS game_event_detail_master (
                                game_id CHAR(12),
                                away_team_id CHAR(3),
                                home_team_id CHAR(3),
                                bat_home_id BOOLEAN NOT NULL,
                                inn_ct SMALLINT,
                                outs_ct SMALLINT,
                                balls_ct SMALLINT,
                                strikes_ct SMALLINT,
                                away_score_ct SMALLINT,
                                home_score_ct SMALLINT,
                                bat_id CHAR(8),
                                pit_id CHAR(8),
                                pos2_fld_id CHAR(8),
                                pos3_fld_id CHAR(8),
                                pos4_fld_id CHAR(8),
                                pos5_fld_id CHAR(8),
                                pos6_fld_id CHAR(8),
                                pos7_fld_id CHAR(8),
                                pos8_fld_id CHAR(8),
                                pos9_fld_id CHAR(8),
                                base1_run_id CHAR(8),
                                base2_run_id CHAR(8),
                                base3_run_id CHAR(8),
                                event_tx TEXT,
                                leadoff_fl BOOLEAN,
                                ph_fl BOOLEAN,
                                bat_fld_cd SMALLINT,
                                bat_lineup_id SMALLINT,
                                bat_event_fl BOOLEAN,
                                h_cd SMALLINT,
                                sh_fl BOOLEAN,
                                sf_fl BOOLEAN,
                                event_outs_ct SMALLINT,
                                dp_fl BOOLEAN,
                                tp_fl BOOLEAN,
                                rbi_ct SMALLINT,
                                wp_fl BOOLEAN,
                                pb_fl BOOLEAN,
                                fld_cd SMALLINT,
                                battedball_cd SMALLINT,
                                bunt_fl BOOLEAN,
                                foul_fl BOOLEAN,
                                battedball_loc_tx TEXT,
                                err_ct SMALLINT,
                                err_fld_cds SMALLINT[],
                                err_cds CHAR(1)[],
                                bat_dest_id SMALLINT,
                                run1_dest_id SMALLINT,
                                run2_dest_id SMALLINT,
                                run3_dest_id SMALLINT,
                                bat_play_tx TEXT,
                                run1_play_tx TEXT,
                                run2_play_tx TEXT,
                                run3_play_tx TEXT,
                                run1_sb_fl BOOLEAN,
                                run2_sb_fl BOOLEAN,
                                run3_sb_fl BOOLEAN,
                                run1_cs_fl BOOLEAN,
                                run2_cs_fl BOOLEAN,
                                run3_cs_fl BOOLEAN,
                                run1_pk_fl BOOLEAN,
                                run2_pk_fl BOOLEAN,
                                run3_pk_fl BOOLEAN,
                                run1_resp_pit_id CHAR(8),
                                run2_resp_pit_id CHAR(8),
                                run3_resp_pit_id CHAR(8),
                                game_new_fl BOOLEAN,
                                game_end_fl BOOLEAN,
                                pr_run1_fl BOOLEAN,
                                pr_run2_fl BOOLEAN,
                                pr_run3_fl BOOLEAN,
                                removed_for_pr_run1_id CHAR(8),
                                removed_for_pr_run2_id CHAR(8),
                                removed_for_pr_run3_id CHAR(8),
                                removed_for_ph_bat_id CHAR(8),
                                removed_for_ph_bat_fld_cd SMALLINT,
                                po_fld_cds SMALLINT[],
                                ass_fld_cds SMALLINT[],
                                event_id SMALLINT,
                                PRIMARY KEY (game_id, event_id)
                            );"""

