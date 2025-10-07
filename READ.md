# Home Lab — Windows 10 (victim) & Kali Linux (attacker)

## TL;DR
Personal, isolated cyber security lab used to learn Windows logging, basic hardening, and incident response workflows. Contains documentation, sanitized screenshots, and safe automation for log parsing and lab resets.
## Goals
- Practice Windows logging & detection (Event Logs, Sysmon)
- - Practice attacker tools in an isolated environment (Kali)
  - - Build incident response playbooks and simple automation

## Architecture 
See `docs/architecture.md` for a diagram. 
 
 ## What’s included - `docs/` — architecture diagram, sanitized screenshots, walkthroughs 
 - `scripts/` — safe utilities (log parser example)
 - - `playbooks/` — incident response checklists (optional)
   - - `LICENSE` — MIT
  
  ## Reproduce (high level) 
  1. Create an **isolated** virtual network in your hypervisor (VMhost host-only or NAT with no bridged access).
   2. Deploy Windows 10 and Kali VMs on the isolated network.
        3. Configure Windows logging (Event Viewer / Sysmon) and push logs to a collector or save locally.
           4. Run benign tests and collect sanitized logs/screenshots.
 
  > **Note:** This repo contains only sanitized, non-sensitive artifacts. No VM images, credentials, or private keys are included.

> ## Outcomes / Highlights - Enabled Sysmon and captured process creation logs (sample sanitized logs in `docs/`) - Wrote a Python parser to aggregate common event types (see `scripts/parse_events.py`) - Documented an incident response playbook for a suspected PowerShell misuse event

>  ## Contact
> Abu Bakarr Bangura — [LinkedIn](www.linkedin.com/in/abu-bakarr-bangura-675a4635a) •ab.bangura19@gmail.com
