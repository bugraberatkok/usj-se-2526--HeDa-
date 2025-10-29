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

- **Capacity enforcement** — Cannot sell more tickets than capacity  
- **Unique QR codes** — Each ticket has exactly one unique code  
- **Payment before ticket** — Tickets only issued after successful payment  
- **Student verification** — Discounts only for verified university emails  
- **Refund timeframe** — Refunds only allowed >72 hours before event  
- **Event requirements** — Must have name, date, venue, capacity, and at least one price tier before publishing  
- **One-time validation** — Each QR code can only be used once

