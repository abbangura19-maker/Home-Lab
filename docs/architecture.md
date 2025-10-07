# Home Lab Architecture

```mermaid
graph LR
 Internet((Internet)) --> FW[Host Firewall / Router]
 FW --> IsolatedNet[Isolated Virtual Network]
 IsolatedNet --> Kali[Kali Linux (Attacker)]
 IsolatedNet --> Win10[Windows 10 (Victim)]
 IsolatedNet --> SIEM[Log Collector (optional)]
