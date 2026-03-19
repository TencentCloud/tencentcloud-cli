**Example 1: 查询Windows补丁风险列表**

查询Windows补丁风险列表

Input: 

```
tccli cwp DescribeWindowsPatchList --cli-unfold-argument  \
    --Filters.0.Name ShowNew \
    --Filters.0.Values 1 \
    --Filters.1.Name Status \
    --Filters.1.Values 0
```

Output: 
```
{
    "Response": {
        "PatchInfoList": [
            {
                "EffectHostCount": 1,
                "Ids": "73",
                "IsNew": 1,
                "KbId": 7070,
                "KbNo": "KB5062592",
                "KbPreCondition": "",
                "LastScanTime": "2025-07-31 14:28:50",
                "Name": "2025-07 适用于基于 x64 的系统的 Windows Server 2012 月度安全质量汇总（KB5062592）",
                "PublishTime": "2025-07",
                "RelateVulCount": 58,
                "RelateVulList": [
                    "CVE-2023-24932",
                    "CVE-2025-47971",
                    "CVE-2025-47976",
                    "CVE-2025-47984",
                    "CVE-2025-47985",
                    "CVE-2025-47986",
                    "CVE-2025-47987",
                    "CVE-2025-48824",
                    "CVE-2025-49657",
                    "CVE-2025-49658",
                    "CVE-2025-49661",
                    "CVE-2025-49670",
                    "CVE-2025-49671",
                    "CVE-2025-49672",
                    "CVE-2025-49674",
                    "CVE-2025-49676",
                    "CVE-2025-49686",
                    "CVE-2025-49687",
                    "CVE-2025-49689",
                    "CVE-2025-49716",
                    "CVE-2025-49721",
                    "CVE-2025-49753",
                    "CVE-2025-47973",
                    "CVE-2025-47975",
                    "CVE-2025-47980",
                    "CVE-2025-47981",
                    "CVE-2025-47996",
                    "CVE-2025-47998",
                    "CVE-2025-48001",
                    "CVE-2025-48804",
                    "CVE-2025-48805",
                    "CVE-2025-48806",
                    "CVE-2025-48808",
                    "CVE-2025-48814",
                    "CVE-2025-48815",
                    "CVE-2025-48816",
                    "CVE-2025-48817",
                    "CVE-2025-48819",
                    "CVE-2025-48821",
                    "CVE-2025-49659",
                    "CVE-2025-49663",
                    "CVE-2025-49664",
                    "CVE-2025-49665",
                    "CVE-2025-49667",
                    "CVE-2025-49668",
                    "CVE-2025-49669",
                    "CVE-2025-49673",
                    "CVE-2025-49675",
                    "CVE-2025-49678",
                    "CVE-2025-49679",
                    "CVE-2025-49681",
                    "CVE-2025-49683",
                    "CVE-2025-49722",
                    "CVE-2025-49727",
                    "CVE-2025-49729",
                    "CVE-2025-49730",
                    "CVE-2025-49732",
                    "CVE-2025-49742"
                ],
                "RelatedProduct": "Windows Server 2012",
                "Status": 0
            }
        ],
        "RequestId": "02625b85-89d8-4883-a200-4bffb8b1e003",
        "TotalCount": 1
    }
}
```

