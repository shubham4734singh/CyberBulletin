---
title: Authorities disrupt router DNS hijacks used to steal Microsoft 365 logins
date: 2026-04-07
category: [Threat Intelligence, Malware, Data Breach]
thumbnail: 
source_link: https://www.bleepingcomputer.com/news/security/authorities-disrupt-dns-hijacks-used-to-steal-microsoft-365-logins/
---

## ⚡ Quick Summary
An international law enforcement operation has successfully disrupted a campaign known as FrostArmada, which is attributed to the APT28 group. This campaign involved hijacking the DNS settings of MikroTik and TP-Link routers to redirect users to fake Microsoft login pages, with the ultimate goal of stealing Microsoft 365 account credentials. The operation, conducted in partnership with private companies, highlights the collaborative efforts between law enforcement and the private sector to combat sophisticated cyber threats.

## 🛠 Technical Analysis
From a technical standpoint, the FrostArmada campaign leverages a combination of social engineering and exploitation of vulnerabilities in commonly used router models. By compromising the DNS settings of these routers, the attackers can manipulate the traffic flowing through them, redirecting users to malicious sites that mimic the legitimate Microsoft login page. This tactic allows the attackers to capture sensitive login credentials, which can then be used for further malicious activities, such as email phishing, data exfiltration, or lateral movement within an organization's network.

The use of compromised routers as a vector for cyber attacks underscores the importance of securing all aspects of an organization's network infrastructure, not just endpoints and servers. It also highlights the need for regular audits and updates of firmware and software on all network devices to prevent exploitation of known vulnerabilities. Moreover, implementing robust security practices such as multi-factor authentication (MFA) can significantly reduce the risk of credential theft, even in the event of a successful phishing attack.

## 🛡 Mitigation & Impact
To mitigate the risk of falling victim to similar DNS hijacking campaigns, individuals and organizations should ensure that their routers are updated with the latest firmware and that default passwords are changed. Regularly monitoring network traffic for suspicious activity and educating users about the dangers of phishing attacks can also help in early detection and prevention of such threats.

The impact of the disruption of the FrostArmada campaign is twofold. Firstly, it directly protects Microsoft 365 users from credential theft, safeguarding their sensitive data and preventing potential financial and reputational damage. Secondly, it sends a strong message to cybercriminal groups about the determination and capability of international law enforcement and private sector partners to collaborate and take down sophisticated cyber threats. This collaborative approach is crucial in the ongoing battle against cybercrime, as it combines resources, expertise, and reach to dismantle complex criminal operations that transcend national borders.