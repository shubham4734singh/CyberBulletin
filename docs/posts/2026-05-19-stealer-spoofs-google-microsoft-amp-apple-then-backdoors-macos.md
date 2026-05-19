---
title: Stealer Spoofs Google, Microsoft & Apple, Then Backdoors macOS
date: 2026-05-19
category: [Threat Intelligence, Malware]
thumbnail: assets/images/2026-05-19-stealer-spoofs-google-microsoft-amp-apple-then-backdoors-macos.png
source_link: https://www.darkreading.com/threat-intelligence/stealer-spoofs-google-microsoft-apple-backdoors-macos
---

## ⚡ Quick Summary
The SHub Reaper stealer has been identified as a new threat that spoofs major tech companies such as Google, Microsoft, and Apple. This malware is distributed through fake installers of popular applications like WeChat and Miro. The stealer marks a significant shift in tactics, utilizing Apple scripts for execution instead of relying on traditional ClickFix social engineering methods. This change in strategy allows the malware to backdoor macOS systems, posing a substantial threat to users who may unknowingly install the fake software.

## 🛠 Technical Analysis
From a technical standpoint, the SHub Reaper stealer's ability to mimic legitimate installers and use Apple scripts for execution demonstrates a level of sophistication. This approach enables the malware to evade detection by traditional security measures, as it does not rely on common executable files that are typically flagged by antivirus software. The use of Apple scripts also indicates that the attackers are targeting macOS systems specifically, exploiting the trust users have in these scripts as a means to bypass security controls. The fact that the malware can spoof well-known companies like Google, Microsoft, and Apple suggests a high level of social engineering expertise, as the attackers are successfully creating convincing fake installers that can deceive even cautious users.

## 🛡 Mitigation & Impact
To mitigate the threat posed by the SHub Reaper stealer, users must be vigilant when downloading and installing software. It is crucial to only download applications from official sources and to verify the authenticity of installers before proceeding with the installation process. Moreover, macOS users should be cautious when encountering Apple scripts, as these can now be used as a vector for malware execution. The impact of this malware can be significant, as it not only compromises user data but also establishes a backdoor into the infected system, allowing attackers to maintain access and potentially escalate privileges. Organizations and individuals must prioritize educating users about these threats and implementing robust security measures, including regular software updates, antivirus scans, and network monitoring to detect and respond to such attacks.