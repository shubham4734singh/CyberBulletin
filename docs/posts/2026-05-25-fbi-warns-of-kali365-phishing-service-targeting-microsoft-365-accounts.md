---
title: FBI warns of Kali365 phishing service targeting Microsoft 365 accounts
date: 2026-05-25
category: [Threat Intelligence, Malware]
thumbnail: 
source_link: https://www.bleepingcomputer.com/news/security/fbi-warns-of-kali365-phishing-service-targeting-microsoft-365-accounts/
---

## ⚡ Quick Summary
The FBI has issued a warning about Kali365, a phishing-as-a-service platform (PhaaS) that targets Microsoft 365 accounts. This platform exploits OAuth device code authentication to steal session tokens, effectively bypassing multi-factor authentication (MFA) and gaining unauthorized access to Microsoft 365 accounts. The Kali365 service poses a significant threat to organizations relying on Microsoft 365 for their daily operations, as it can lead to data breaches, unauthorized data access, and other malicious activities.

## 🛠 Technical Analysis
From a technical standpoint, the Kali365 phishing service leverages a sophisticated approach to bypass security measures. By abusing OAuth device code authentication, attackers can trick users into granting access to their Microsoft 365 accounts without needing to intercept or crack passwords. This method exploits the trust established between the user, Microsoft, and the device, creating a vector for phishing attacks that can evade traditional security controls. The fact that Kali365 can bypass MFA highlights the evolving nature of phishing threats and the need for continuous monitoring and adaptation of security strategies. As a cybersecurity expert, it's clear that the success of Kali365 depends on social engineering tactics to deceive users into initiating the authentication flow, underscoring the importance of user awareness and education in preventing such attacks.

## 🛡 Mitigation & Impact
To mitigate the risks associated with the Kali365 phishing service, organizations should prioritize user education and awareness campaigns to help employees recognize and avoid phishing attempts. Implementing additional security controls, such as conditional access policies and enhanced monitoring of Microsoft 365 account activity, can also help detect and respond to potential compromises. The impact of Kali365 on an organization can be severe, including data theft, financial loss, and reputational damage. Therefore, proactive measures such as regularly reviewing account permissions, leveraging advanced threat protection tools, and ensuring that all users understand the risks and consequences of phishing attacks are crucial. By taking a multi-layered approach to security that combines technical controls with user awareness, organizations can reduce their vulnerability to the Kali365 phishing service and similar threats.