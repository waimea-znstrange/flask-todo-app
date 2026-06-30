#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class TaskTable:

    NAME = "tasks"

    SCHEMA = """
        CREATE TABLE tasks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            priority    INTEGER NOT NULL DEFAULT 3,
            complete    BOOLEAN NOT NULL DEFAULT 0
        )
    """

    SEED_DATA = """
        INSERT INTO tasks (id, name, priority, complete)
        VALUES
            ("Feed the dog",  "1")
            ("Do the dishes", "2"),
            ("Pet the cat",   "3"),
    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1,
#     Table2,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
#       foreign keys AFTER the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    TaskTable,
    # Add more tables here...
]

