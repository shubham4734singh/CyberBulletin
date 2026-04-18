---
title: Tycoon 2FA Phishers Scatter, Adopt Device Code Phishing
date: 2026-04-18
category: [Threat Intelligence, Malware]
thumbnail: assets/images/2026-04-18-tycoon-2fa-phishers-scatter-adopt-device-code-phishing.jpg
source_link: https://www.darkreading.com/threat-intelligence/tycoon-2fa-hackers-device-code-phishing
---

## ⚡ Quick Summary
The Tycoon 2FA phishers have recently shifted their tactics, adopting a new method known as device code phishing. This approach involves tricking victims into providing account access by exploiting a service's legitimate new-device login flow. By doing so, attackers can bypass traditional two-factor authentication (2FA) mechanisms, potentially leading to unauthorized account access and data breaches.

## 🛠 Technical Analysis
From a technical standpoint, device code phishing is a clever tactic that leverages the trust users have in legitimate services. When a user attempts to log in from a new device, the service may send a verification code to the user's registered email or phone number. However, in the case of device code phishing, the attacker manipulates this process by initiating the new-device login flow themselves. The victim, unaware of the ongoing phishing attempt, may inadvertently provide the verification code to the attacker, granting them access to the account. This technique is particularly concerning, as it targets the user's trust in the service's security mechanisms, rather than exploiting a specific vulnerability.

## 🛡 Mitigation & Impact
To mitigate the risk of device code phishing, users and organizations must be vigilant and implement additional security measures. This includes educating users about the risks of phishing and the importance of verifying the authenticity of login requests. Services can also implement measures such as requiring users to provide additional verification information or using more robust authentication mechanisms, like Universal 2nd Factor (U2F) or WebAuthn. The impact of device code phishing can be significant, as it may lead to unauthorized access to sensitive data, financial loss, and reputational damage. As such, it is essential for cybersecurity professionals to stay informed about emerging threats and adapt their security strategies to protect against these evolving tactics.