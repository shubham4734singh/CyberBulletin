---
title: Tycoon2FA hijacks Microsoft 365 accounts via device-code phishing
date: 2026-05-17
category: [Threat Intelligence, Malware]
thumbnail: 
source_link: https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/
---

## ⚡ Quick Summary
The Tycoon2FA phishing kit has been upgraded to include device-code phishing capabilities, allowing attackers to hijack Microsoft 365 accounts. This new technique abuses Trustifi click-tracking URLs to bypass traditional security measures. As a result, organizations using Microsoft 365 should be aware of this emerging threat and take necessary precautions to protect their accounts.

## 🛠 Technical Analysis
From a technical perspective, the Tycoon2FA phishing kit's ability to conduct device-code phishing attacks is particularly concerning. Device-code phishing involves tricking victims into providing a verification code sent to their device, which is then used to authenticate the attacker's access to the targeted account. By leveraging Trustifi click-tracking URLs, the attackers can obscure the phishing link's true destination, making it more difficult for security software to detect the threat. This highlights the importance of implementing robust security controls, such as conditional access policies and multi-factor authentication (MFA) solutions that are resistant to phishing attacks.

## 🛡 Mitigation & Impact
To mitigate the risk of Tycoon2FA phishing attacks, organizations should educate their users about the dangers of device-code phishing and the importance of verifying the authenticity of requests for verification codes. Additionally, implementing advanced security controls, such as behavioral analytics and anomaly detection, can help identify and block suspicious activity. The impact of a successful Tycoon2FA phishing attack could be significant, potentially resulting in unauthorized access to sensitive data and disruption of business operations. As such, it is essential for organizations to prioritize the security of their Microsoft 365 accounts and take proactive measures to prevent and detect phishing attacks.