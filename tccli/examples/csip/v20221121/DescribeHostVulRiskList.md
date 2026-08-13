**Example 1: 获取漏洞风险列表**

获取漏洞风险列表

Input: 

```
tccli csip DescribeHostVulRiskList --cli-unfold-argument  \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Limit 10 \
    --Offset 0 \
    --Order desc \
    --By LatestScanTime
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Account": [
                    {
                        "AppID": 260083796,
                        "Nick": "700002365149",
                        "Uin": "700002365149"
                    }
                ],
                "DefendStatus": "NOT_ENABLED",
                "EffectHostCount": 1,
                "LatestScanTime": "2026-06-12T08:15:45Z",
                "RiskID": 45230,
                "RiskStatus": "PENDING",
                "VulDetail": {
                    "AffectProduct": [
                        "socat"
                    ],
                    "AffectVendor": [
                        "dest-unreach"
                    ],
                    "CVEID": "CVE-2024-54661",
                    "CVSSLevel": "LOW",
                    "Category": "LINUX",
                    "CheckMethod": "VersionCompare",
                    "CvssScore": 9.8,
                    "DefendHostCount": 0,
                    "DefendStatus": "NOT_ENABLED",
                    "EPSSScore": 0.00164,
                    "FixSolution": "建议关注厂商公告或升级到最新版本。",
                    "ID": 45230,
                    "KVERecord": false,
                    "KVERecordTime": "",
                    "Label": [],
                    "LatestScanTime": "",
                    "LatestTrend": [],
                    "Mechanism": "",
                    "Name": "socat 安全漏洞(CVE-2024-54661)",
                    "NotDefendHostCount": 0,
                    "Precondition": "",
                    "PublishTime": "2024-12-04 13:15:00",
                    "RefLink": "https://repo.or.cz/socat.git/blob/6ff391324d2d3b9f6bfb58e7d16a20be43b47af7:/readline.sh#l29",
                    "Remark": "",
                    "Summary": "socat是socat开源的一个中继器，用于在两个独立的数据之间进行双向数据传输渠道。 socat 1.8.0.1及之前版本存在安全漏洞，该漏洞源于readline.sh依赖于/tmp/$USER/stderr2文件。",
                    "SupportFix": true,
                    "VRPRatingInfo": {
                        "Remark": "",
                        "Result": "",
                        "Stage": [
                            {
                                "Result": "",
                                "Stage": "威胁活跃度"
                            }
                        ]
                    },
                    "VulAffect": []
                }
            }
        ],
        "TotalCount": 706,
        "RequestId": "d224b5c5-013c-427e-a7ea-0b2e780da55f"
    }
}
```

