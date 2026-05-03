---
title: Microsoft Defender wrongly flags DigiCert certs as Trojan:Win32/Cerdigent.A!dha
date: 2026-05-03
category: [Threat Intelligence, Malware]
thumbnail: 
source_link: https://www.bleepingcomputer.com/news/security/microsoft-defender-wrongly-flags-digicert-certs-as-trojan-win32-cerdigentadha/
---

## ⚡ Quick Summary
A recent issue has been reported with Microsoft Defender, where it is incorrectly identifying legitimate DigiCert root certificates as Trojan:Win32/Cerdigent.A!dha. This has resulted in a significant number of false-positive alerts, and in some cases, the removal of certificates from Windows systems. The incorrect flagging of these certificates can cause disruptions to system operations and may lead to issues with secure communication protocols.

## 🛠 Technical Analysis
From a technical standpoint, the misidentification of DigiCert certificates as malware suggests a potential issue with the signature-based detection mechanisms employed by Microsoft Defender. It is possible that the antivirus software is relying on outdated or flawed signatures, leading to the false positives. Additionally, the fact that the certificates are being flagged as Trojan:Win32/Cerdigent.A!dha, a specific type of malware, implies that the detection algorithm is not adequately distinguishing between legitimate and malicious code. As a cybersecurity expert, it is essential to continuously update and refine detection models to minimize the occurrence of such false positives, which can erode trust in the security solution and cause unnecessary downtime.

## 🛡 Mitigation & Impact
The impact of this issue can be significant, as the removal of legitimate certificates can disrupt secure communication protocols, such as TLS, and potentially lead to system crashes or failures. To mitigate this issue, system administrators and users should be cautious when encountering alerts related to DigiCert certificates and verify the legitimacy of the certificates before taking any action. Microsoft should also take immediate action to update its detection signatures and algorithms to prevent such false positives. Furthermore, organizations should have incident response plans in place to quickly respond to and contain the impact of such events, ensuring minimal disruption to their operations. It is also crucial for Microsoft to communicate clearly with its customers about the issue, the steps being taken to resolve it, and any temporary workarounds that can be applied until a permanent fix is available.