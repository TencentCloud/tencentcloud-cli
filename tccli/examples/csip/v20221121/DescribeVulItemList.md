**Example 1: 获取漏洞检测项列表**

获取漏洞检测项列表

Input: 

```
tccli csip DescribeVulItemList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Order desc \
    --By PublishTime
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AffectProduct": [],
                "AffectVendor": [],
                "CVEID": "CVE-2026-8863",
                "CVSSLevel": "HIGH",
                "Category": "WINDOWS",
                "CheckMethod": "VersionCompare",
                "CvssScore": 7.8,
                "DefendHostCount": 0,
                "DefendStatus": "NOT_ENABLED",
                "EPSSScore": 0,
                "FixSolution": "1. 升级版本：微软已发布修复该漏洞的安全更新，请评估业务影响后，尽快安装 Windows 官方发布的安全补丁以修复 UEFI Secure Boot 保护机制缺陷。",
                "ID": 123044,
                "KVERecord": false,
                "KVERecordTime": "",
                "Label": [],
                "LatestScanTime": "",
                "LatestTrend": [],
                "Mechanism": "",
                "Name": "Microsoft UEFI SHIM 安全启动绕过漏洞(CVE-2026-8863)",
                "NotDefendHostCount": 0,
                "Precondition": "",
                "PublishTime": "2026-06-10 02:10:15",
                "RefLink": "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-8863,https://kb.cert.org/vuls/id/616257,https://nvd.nist.gov/vuln/detail/CVE-2026-8863,https://vuldb.com/vuln/369783,https://www.tenable.com/blog/microsofts-june-2026-patch-tuesday-addresses-198-cves-cve-2026-49160-cve-2026-50507,https://www.kb.cert.org/vuls/id/616257,https://github.com/advisories/GHSA-4hqv-6cp5-4rq9,https://exchange.xforce.ibmcloud.com/vulnerabilities/YX3srZ4BC7vCu9U8jfyM,https://www.wiz.io/vulnerability-database/cve/cve-2026-8863,https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2026-8863,https://www.tenable.com/cve/CVE-2026-8863",
                "Remark": "",
                "Summary": "多个由微软签名的 UEFI SHIM 引导加载程序存在安全启动（Secure Boot）绕过漏洞。拥有管理员权限或能够修改引导过程的攻击者，可以利用这些存在漏洞的 SHIM 引导加载程序，在操作系统加载之前绕过安全启动保护并执行任意代码。必须应用特定的 UEFI DBX（禁止列表）更新以阻止这些存在漏洞的引导加载程序。",
                "SupportFix": false,
                "VRPRatingInfo": {
                    "Remark": "",
                    "Result": "",
                    "Stage": []
                },
                "VulAffect": []
            }
        ],
        "TotalCount": 70080,
        "RequestId": "2589e236-89fa-4379-882a-d5e675c2e8f7"
    }
}
```

