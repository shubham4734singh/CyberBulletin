---
title: "VS Code zero-day lets hackers steal GitHub tokens in one click"
date: 2026-06-03
category: [Vulnerabilities, Threat Intelligence]
thumbnail: ""
source_link: "https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/"
---

## ⚡ Quick Summary
A recently discovered zero-day vulnerability in Visual Studio Code (VS Code) has been found to allow attackers to steal GitHub authentication tokens. This is achieved by tricking users into clicking a malicious link, which then exploits the vulnerability to gain unauthorized access to the user's GitHub account. The exploit code for this vulnerability has been released, highlighting the urgency for users and developers to take immediate action to protect themselves.

## 🛠 Technical Analysis
From a technical standpoint, this vulnerability exploits a weakness in VS Code's handling of links, allowing attackers to craft a malicious link that, when clicked, triggers the exploit. The exploit then steals the user's GitHub authentication token, which can be used to access the user's GitHub account without their knowledge or consent. This type of attack is particularly dangerous because it requires minimal user interaction—just a single click on a link. The fact that exploit code is publicly available increases the risk, as it lowers the barrier for potential attackers, making it more likely that the vulnerability will be widely exploited.

## 🛡 Mitigation & Impact
To mitigate this vulnerability, VS Code users, especially those who use GitHub, should exercise extreme caution when clicking on links, especially those that seem suspicious or come from unknown sources. Until a patch is released, users can consider using alternative code editors or taking steps to limit the damage an attacker could do with a stolen GitHub token, such as enabling two-factor authentication (2FA) on their GitHub account and regularly reviewing account activity for any signs of unauthorized access. The impact of this vulnerability could be significant, given the widespread use of VS Code among developers and the potential for attackers to access sensitive code repositories. It underscores the importance of keeping software up to date and being vigilant about security vulnerabilities in the tools developers use daily.