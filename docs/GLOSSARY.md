# 📝 Glossary – HeDa Domain

Aşağıdaki tablo, kod tabanımızdaki varlıklar (Entities) ve değer nesneleri (Value Objects) ile tutarlılığı sağlamak amacıyla güncellenmiştir. Yapılan ana değişiklikler, özellikle "Report Category" teriminin "Report Reason" olarak değiştirilmesi ve "Donation Amount" teriminin eklenmesidir.

| **Term** | **Definition** | **Example** |
| :--- | :--- | :--- |
| **User** | A registered person who participates in debates or interacts with the platform. | `User#U-1045` responds to a debate thread. |
| **Donator** | A person who contributes financial support through the external donation system. **It is represented in the system by the associated payment details for a specific Donation transaction.** | `Donator#D-2203` donates 10€ via GoFoundMe API. |
| **Moderator** | Authorized staff who reviews and manages reported or suspicious content. | `Moderator#M-101` removes an offensive comment. |
| **Debate** | A public discussion topic where users share opinions and arguments. | “AI replacing human jobs” debate created by User#U-1532. |
| **Conversation Data** | Stored message logs and metadata from debates. | Debates log shows 42 messages exchanged on Oct 15th. |
| **Report** | A user or AI-generated complaint about inappropriate behavior or content. **The report can target a User's behavior or specific Content (e.g., a message or debate).** | User#U-240 submits a report for hate speech. |
| **Report Reason** (Değiştirildi: Eskiden 'Report Category' idi) | **The specific classification or reason for a report.** | Report marked under “Harassment / Abuse”. |
| **Suspicious Activity** | Behavior automatically flagged by the AI moderation system for human review. | AI detects repeated spam messages and flags User#U-523. |
| **Donation** | A financial transaction processed via the external donation tool. | Donation `TXN-2025-0782` of 25€ completed successfully. |
| **Donation Amount** (Yeni Terim) | **The specific monetary value of a donation.** | A donation amount of 10.00€ is processed. |
| **Payment Result** | The outcome of a donation transaction indicating success or failure. | Payment result: “Success” for TXN-2025-0782. |
| **Data Report** | Analytical summary of system usage, activity, or moderation statistics. | Daily report shows 312 new debates and 54 reports. |
| **Data Analyst** | Staff member who reviews platform analytics and trends via dashboard. | Analyst reviews engagement statistics for October. |
