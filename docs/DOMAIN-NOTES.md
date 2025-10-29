# Domain Notes - HeDa

## Host Container 

  The most suitable container of our C2 diagram to be the domain host is HeDa API [Backend APP]


## Key Behaviors
**Users**
- Make a donation
- Create an account
- Login to an account
- Create a debat
- Respond to a debate

**Access Control Staff / Moderators**
- Browse events  
- Purchase tickets with discounts  
- Receive QR codes  
- Request refunds

**Data Analysts**
- Create and publish events  
- Configure pricing  
- Monitor sales

**Donator**
- Process payments  
- Generate QR codes  
- Validate entries  
- Enforce capacity limits

---

## Critical Invariants

- **Capacity enforcement** — Cannot sell more tickets than capacity  
- **Unique QR codes** — Each ticket has exactly one unique code  
- **Payment before ticket** — Tickets only issued after successful payment  
- **Student verification** — Discounts only for verified university emails  
- **Refund timeframe** — Refunds only allowed >72 hours before event  
- **Event requirements** — Must have name, date, venue, capacity, and at least one price tier before publishing  
- **One-time validation** — Each QR code can only be used once

