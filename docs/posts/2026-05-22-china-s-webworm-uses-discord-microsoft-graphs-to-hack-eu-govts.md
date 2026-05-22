---
title: China's Webworm Uses Discord, Microsoft Graphs to Hack EU Govts.
date: 2026-05-22
category: [Threat Intelligence, Malware]
thumbnail: assets/images/2026-05-22-china-s-webworm-uses-discord-microsoft-graphs-to-hack-eu-govts.jpg
source_link: https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs
---

## ⚡ Quick Summary
A recently discovered advanced persistent threat (APT) group, known as China's Webworm, has been found exploiting unconventional methods to infiltrate European government networks. This group leverages platforms like Discord and Microsoft Graphs, along with SOCKS proxies such as SoftEther VPN, to carry out their attacks. The use of these tools enables the attackers to create complex networks that act as intermediaries between the victims and the attackers themselves, making detection and tracing of the malicious activities highly challenging.

## 🛠 Technical Analysis
From a technical standpoint, the incorporation of Discord and Microsoft Graphs into the Webworm's arsenal signifies a sophisticated approach to cyber espionage. Discord, primarily known as a communication platform for communities, can be repurposed by attackers to manage command and control (C2) operations due to its real-time messaging capabilities and file-sharing features. Similarly, Microsoft Graphs, designed to provide a unified programmability model for accessing the tremendous amount of data in Microsoft 365, can be exploited to gain deep insights into a target's infrastructure and facilitate lateral movement within a compromised network.

The employment of SOCKS proxies like SoftEther VPN adds another layer of complexity to these operations. By utilizing such proxies, the attackers can conceal their IP addresses and make it appear as though the malicious traffic is originating from different, potentially innocuous sources. This technique significantly complicates the process of attributing the attacks to the actual perpetrators and hampers the ability of security teams to block the malicious traffic effectively.

## 🛡 Mitigation & Impact
To mitigate such advanced threats, it's crucial for organizations, especially those in the government sector, to implement multi-layered security strategies. This includes enhancing network monitoring capabilities to detect anomalous traffic patterns, enforcing strict access controls, and regularly updating software to patch known vulnerabilities. Additionally, adopting a zero-trust security model can help minimize the impact of a breach by limiting the ability of attackers to move laterally within the network.

The impact of these attacks can be profound, with potential consequences including the theft of sensitive information, disruption of critical services, and erosion of public trust in government institutions. Therefore, it's essential for cybersecurity professionals to stay informed about the evolving tactics, techniques, and procedures (TTPs) of APT groups like China's Webworm and to continually assess and improve their organization's defenses against such threats. Regular security awareness training for employees, coupled with the deployment of advanced threat detection tools, can also play a critical role in preventing and responding to these sophisticated cyber attacks.