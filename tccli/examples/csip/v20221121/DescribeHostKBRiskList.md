**Example 1: 获取kb风险概览**

获取kb风险概览

Input: 

```
tccli csip DescribeHostKBRiskList --cli-unfold-argument  \
    --MemberId mem-*******-6f5795752f66e429 \
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
                        "AppID": 260082268,
                        "Nick": "成员账号",
                        "Uin": "700002332361"
                    }
                ],
                "EffectHostCount": 2,
                "KBDetail": {
                    "ID": 791,
                    "Name": "2026-适用于 Microsoft server operating system version 21H2 的 04 累积更新，适合基于 x64 的系统 (KB5082142)",
                    "NeedRestart": true,
                    "Number": "KB5082142",
                    "PublishTime": "2026-04-01 00:00:00",
                    "ReferUrl": "https://support.microsoft.com/help/5082142",
                    "RelateVulCount": 115,
                    "RelateVulList": [
                        {
                            "CVEID": "CVE-2026-20930",
                            "CvssScore": 7.8,
                            "Label": [],
                            "Level": "HIGH",
                            "PublishTime": "2026-04-15 02:16:00",
                            "VulID": 121960,
                            "VulName": "Microsoft Windows 竞争条件问题漏洞(CVE-2026-20930)"
                        }
                    ]
                },
                "LatestScanTime": "2026-06-08T06:30:30Z",
                "RiskID": 791,
                "RiskStatus": "PENDING"
            }
        ],
        "TotalCount": 2,
        "RequestId": "126b1d8d-43e6-41eb-b742-937f2bbd0514"
    }
}
```

