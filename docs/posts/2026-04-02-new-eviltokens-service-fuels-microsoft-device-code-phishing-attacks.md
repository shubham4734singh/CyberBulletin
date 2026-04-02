---
title: New EvilTokens service fuels Microsoft device code phishing attacks
date: 2026-04-02
category: [Threat Intelligence, Malware]
thumbnail: 
source_link: https://www.bleepingcomputer.com/news/security/new-eviltokens-service-fuels-microsoft-device-code-phishing-attacks/
---

## ⚡ Quick Summary
A recently discovered malicious kit, known as EvilTokens, has been identified as a significant threat to Microsoft accounts. This kit integrates device code phishing capabilities, enabling attackers to hijack accounts and conduct advanced business email compromise (BEC) attacks. The EvilTokens service is particularly dangerous because it streamlines the process of phishing for device codes, which are typically used for authentication purposes, such as in Microsoft's multi-factor authentication (MFA) process. By leveraging this service, attackers can bypass traditional security measures designed to protect user accounts.

## 🛠 Technical Analysis
From a technical standpoint, the EvilTokens service represents a sophisticated evolution in phishing tactics. By targeting device codes, attackers exploit a vulnerability that many users might not be aware of, especially given the increasing reliance on MFA to secure access to sensitive information. The kit likely includes tools for generating phishing pages that mimic Microsoft's official pages, tricks for convincing victims to input their device codes, and mechanisms for quickly exploiting these codes before they expire. This level of sophistication suggests that the attackers behind EvilTokens have a deep understanding of Microsoft's authentication mechanisms and have developed a method to exploit them efficiently. Furthermore, the integration of this capability with BEC attacks indicates a broader strategy aimed at financial gain through targeted fraud.

## 🛡 Mitigation & Impact
To mitigate the risks associated with the EvilTokens service, users and organizations must prioritize education and vigilance. This includes training employees to recognize and avoid phishing attempts, especially those targeting device codes. Implementing additional security layers beyond MFA, such as conditional access policies based on user and device risk profiles, can also help in reducing the impact of such attacks. Moreover, organizations should monitor their systems for signs of unauthorized access and have incident response plans in place to quickly respond to potential breaches. The impact of EvilTokens can be significant, ranging from individual account compromise to large-scale BEC attacks that can result in substantial financial losses. As such, proactive measures to prevent these attacks are crucial, including keeping software up to date, using anti-phishing tools, and conducting regular security audits to identify and address vulnerabilities before they can be exploited.