**Example 1: 查询某个组件的CVE信息列表**

查询组件busybox 1.30.0的CVE信息列表。

Input: 

```
tccli bsca DescribeCVEList --cli-unfold-argument  \
    --AnalysisId 4a49ab59-cea9-4d19-bed3-326a27465d92 \
    --ComponentName busybox \
    --ComponentVersion 1.30.1
```

Output: 
```
{
    "Response": {
        "CVESet": [
            {
                "CVEId": "CVE-2018-1000500",
                "Name": "Busybox 安全漏洞",
                "CVSSRank": "HIGH",
                "Category": "web应用漏洞",
                "CVSS": 8.1,
                "CnnvdId": "CVE-2018-1000500",
                "Status": "NONE",
                "FileList": [
                    "/path/busybox"
                ],
                "Description": "Busybox contains a Missing SSL certificate validation vulnerability in The \"busybox wget\" applet that can result in arbitrary code execution. This attack appear to be exploitable via Simply download any file over HTTPS using \"busybox wget https://compromised-domain.com/important-file\".",
                "Solution": "升级到最新无漏洞版本",
                "Defense": "目前厂商已发布升级补丁以修复漏洞，补丁获取链接：https://git.busybox.net/busybox/tree/networking/wget.c?id=8bc418f07eab79a9c8d26594629799f6157a9466#n74",
                "ReferenceList": [
                    "http://lists.busybox.net/pipermail/busybox/2018-May/086462.html",
                    "https://git.busybox.net/busybox/tree/networking/wget.c?id=8bc418f07eab79a9c8d26594629799f6157a9466#n74"
                ],
                "CVSSV3Info": {
                    "CVSS": 8.1,
                    "AttackVector": "NETWORK",
                    "AttackComplexity": "HIGH",
                    "PrivilegesRequired": "NONE",
                    "UserInteraction": "NONE",
                    "Scope": "UNCHANGED",
                    "ConImpact": "HIGH",
                    "IntegrityImpact": "HIGH",
                    "AvailabilityImpact": "HIGH"
                },
                "CVSSV2Info": {
                    "CVSS": 6.8,
                    "AccessVector": "NETWORK",
                    "AccessComplexity": "MEDIUM",
                    "Authentication": "NONE",
                    "ConImpact": "PARTIAL",
                    "IntegrityImpact": "PARTIAL",
                    "AvailabilityImpact": "PARTIAL"
                }
            }
        ],
        "RequestId": "9a113694-6fd9-4c6e-b890-ffad6660c33d"
    }
}
```

