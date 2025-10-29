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

**Donators**
- Process payments 
- Receive payment feedback

---

## Critical Invariants
- **Minimum characters** - Cannot respond or create a debate with blank text
- **Minimum Payment** - Cannot do a null payment

---


## Entity vs Value Object

### Entities

| Entity | Why it's an Entity |
|--------|-------------------|
| **User** | Has unique ID, lifecycle (Interacting → banned → unbanned), state changes as users interact |
| **Moderator** | Has unique identifier, lifecycle (currently working → paid → on break) |
| **Donator** | He is identifiable using his payment informations, He is also related to donation ID |
| **Debate** | Has unique ID, can have many states like 'ongoing' / 'empty' (when no-one but you is part of it)|
| **Report** | Has unique ID, tracking who reported who for what reasons |
| **Donation** | Has unique transaction ID, tracks payment lifecycle |

### Value Objects

| Value Object | Why it's a Value Object |
|--------------|------------------------|
| **Money** | Compared by amount + currency, immutable, no identity |
| **Capacity** | Just a number constraint, replaceable |
| **PriceTier** | Configuration data, compared by values not identity |
| **StudentDiscount** | Discount rules, interchangeable if same percentage |
| **TicketCode** | The data itself is immutable, identity belongs to Ticket |
| **EventDetails** | Descriptive information, no independent identity |
| **RefundPolicy** | Set of rules, compared by value |
| **PaymentStatus** | Enumeration of states, no identity |
