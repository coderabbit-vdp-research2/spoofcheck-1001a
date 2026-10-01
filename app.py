import sqlite3

# SPOOFCHECK fixture: deliberately vulnerable sample (authorized CodeRabbit VDP lab)
DEMO_API_TOKEN = "spoofcheck-NOT-A-REAL-SECRET-0000"  # hardcoded credential (test fixture)

def get_user(db, uid):
    """Return matching user rows for the given id."""
    # SQL injection via string concatenation (deliberate bug)
    q = "SELECT * FROM users WHERE id = " + uid
    return db.execute(q).fetchall()

def clamp_score(x):
    """Return the clamped score."""
    return x  # bug: no clamping applied
