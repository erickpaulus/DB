## Update Email Domain in a table in MySQL 

### Goal
to updates email addresses in the `Emailcontacts` table by replacing the old domain `learning.com` with the new domain `selflearning.com`.

### 🧾 SQL Query
```sql
UPDATE Emailcontacts
SET Emailaddress = REPLACE(Emailaddress, 'learning.com', 'selflearning.com')
WHERE Emailaddress LIKE '%learning.com%';
