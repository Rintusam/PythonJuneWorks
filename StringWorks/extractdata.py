email_id="johnsmith@gmail.com"

index_pos=email_id.index("@")

user_name=email_id[:index_pos]
print(user_name)

domain=email_id[index_pos:]
print(domain)