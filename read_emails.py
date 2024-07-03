from simplegmail import Gmail
from simplegmail.query import construct_query
gmail = Gmail()
query_params = {
    "newer_than": (20, "day"),
    "older_than": (15, "day"),

}

messages = gmail.get_messages(query=construct_query(query_params))
with open("email_samples.txt", "a ") as f:
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Preview: " + message.snippet)
        
        if message.plain:
            if len(message.plain) < 1000:
                f.write(message.plain + "\n")