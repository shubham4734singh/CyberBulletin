---
title: "The silent “Storm”: New infostealer hijacks sessions, decrypts server-side"
date: 2026-04-13
category: [Threat Intelligence, Malware]
thumbnail: ""
source_link: "https://www.bleepingcomputer.com/news/security/the-silent-storm-new-infostealer-hijacks-sessions-decrypts-server-side/"
---

## ⚡ Quick Summary
A newly discovered infostealer, dubbed "Storm", has been found to hijack sessions and decrypt data server-side, allowing attackers to bypass passwords and multi-factor authentication (MFA). Unlike traditional infostealers that decrypt data locally, Storm sends browser data to attacker-controlled servers for decryption. This approach enables the attackers to access sensitive information without being detected by traditional security measures.

## 🛠 Technical Analysis
From a technical standpoint, Storm's ability to decrypt data server-side is a significant enhancement to traditional infostealer tactics. By avoiding local decryption, Storm reduces the risk of detection by endpoint security solutions that typically monitor for suspicious activity on the local machine. The use of server-side decryption also allows attackers to centralize their operations, making it easier to manage and process stolen data. Furthermore, the fact that Storm can bypass MFA highlights the importance of implementing additional security controls, such as behavioral analysis and anomaly detection, to identify and prevent such attacks.

## 🛡 Mitigation & Impact
The discovery of Storm underscores the need for organizations to reassess their security posture and implement measures to prevent such attacks. To mitigate the risk of Storm and similar infostealers, organizations should consider implementing robust browser security controls, such as browser isolation and content filtering, to prevent attackers from intercepting sensitive data. Additionally, organizations should prioritize the use of advanced threat detection and response tools, such as endpoint detection and response (EDR) and security information and event management (SIEM) systems, to identify and respond to potential security incidents. The impact of Storm and similar attacks can be significant, resulting in data breaches, financial loss, and reputational damage, emphasizing the importance of proactive security measures to prevent such incidents.