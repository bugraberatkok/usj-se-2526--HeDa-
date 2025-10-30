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
- **Categorize report** - User cannot report without specifying the category
- **Review report** - Report must be reviewed by a moderator before a sanction
- **Mandatory login** - User cannot report or post without being connected
- **Payment feedback** - Donation must lead to a payment result
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
| **DataReport** | Has unique ID, it can be currently fetching data or 'sent to data analyst' |

### Value Objects

| Value Object | Why it's a Value Object |
|--------------|------------------------|
| **ReportReason** | always a different reason filed in a report (e.g, 'Physical Threats) |
| **DonationMessage** | non essential information, always personalized |
| **DonationAmount** | Numerical data, compared by values not identity |
| **GoodBehaviorPolicy** | Set of rules, things users must follow |
| **ModerationVerdict** | Always a custom reason given by the moderator in reports (e.g., 'Spam', 'Harassment'). |
| **ConversationData** | Represents stored discussion content; identical content means same value. |
| **PaymentResult** | Describes transaction outcome (‘Success’, ‘Failed’, ‘Pending’), no unique ID. |
| **EmailAddress** | Defined purely by its value; identical emails represent the same object. |
| **DataAnalysisContent** | Content of the completed analysis, always different. |

## Bounded Contexts

### 1. Debate Management
**Focus:** Debate creation, participation, and moderation workflows  
**Models:** Debate, Report, Moderator, ReportReason, GoodBehaviorPolicy, ModerationVerdict, ConversationData

### 2. User & Access Control
**Focus:** User identity, authentication, and permissions  
**Models:** User, EmailAddress

### 3. Donations
**Focus:** Financial transactions and donation management  
**Models:** Donation, Donator, PaymentResult, DonationAmount, DonationMessage

### 4. Data Analysis & Reports
**Focus:** Data aggregation and trend analysis  
**Models:** DataReport, DataAnalysisContent
