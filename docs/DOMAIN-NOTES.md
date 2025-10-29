# Domain Notes - HeDa

## Host Container 

  The most suitable container of our C2 diagram to be the domain host is HeDa API [Backend APP]


## Key Behaviors
**Users**
- Browse debates
- Participate in a debate
- Edit your account
- Report inappropriate behaviour 

**Access Control Staff / Moderators**
- Modify features/codes  
- Review reported behaviour
- Erase a report

**Data Analysts**
- Receive data report
- Analyze trends

**Donator**
- Process payments 
- Receive payment feedback

---

## Critical Invariants
- **Minimum characters** - Cannot respond or create a debate with blank text
- **Minimum Payment** - Cannot do a null payment

---

### Entities

| Entity | Why it's an Entity |
|--------|-------------------|
| **User** | Has unique ID, lifecycle (draft → published → open), state changes as tickets sell |
| **Moderator** | Has unique QR code, lifecycle (reserved → paid → validated/refunded) |
| **Donator** | Has persistent identity across multiple purchases |
| **Debate** | Has unique ID, ongoing relationship managing multiple events |
| **Report** | Has unique transaction ID, tracks payment lifecycle |
| **Payment** | Has unique transaction ID, tracks payment lifecycle |
| **Donation** | Has unique transaction ID, tracks payment lifecycle |
