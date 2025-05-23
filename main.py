# Pialago, Nathaniel Christian M.  BSCS601

def session_counter():
    counter = 0
    counter += 1
    print("Session visits: " + str(counter))

session_counter()
session_counter()
session_counter()
session_counter()
session_counter()

def kiosk_usage():
    if not hasattr(kiosk_usage, "total_users"):
        kiosk_usage.total_users = 0
    kiosk_usage.total_users += 1
    print("Total useres today: " + str(kiosk_usage.total_users))

kiosk_usage()
kiosk_usage()
kiosk_usage()
kiosk_usage()
kiosk_usage()
