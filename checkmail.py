#WAP to find if an email is valid or not based on following criteria:
# 1.Must contain "@"
# 2.atleast 1 character before "@"
# 3.atleast 1 character after "@" but before "."
# 4.Atleast 1 character after "."
# 5. Max 256 characters
# 6. Must start with a letter or number

import re
def is_valid_email(email):
  if len(email.split('@')[0])<1:
    return False
  if '@' not in email:
    return False
  part2=email.split('@')[1]
  if len(part2.split('.')[0])<1:
    return False
  if len(part2.split('.')[-1])<1:
    return False
  if len(email)>256:
    return False
  if not email[0].isalnum():
    return False
  return True
email_id="_Sarvesh@xd.xd"
print(is_valid_email(email_id))
