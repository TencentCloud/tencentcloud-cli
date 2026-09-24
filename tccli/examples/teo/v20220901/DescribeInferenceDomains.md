**Example 1: 查询推理域名列表。**



Input: 

```
tccli teo DescribeInferenceDomains --cli-unfold-argument  \
    --ZoneId zone-3v0yhgt4m1z9 \
    --ServiceId inf-vs06pb1cdz61 \
    --SortBy CreateTime \
    --SortOrder Desc \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Domains": [
            {
                "AuthSwitch": "On",
                "Cname": "",
                "CreateTime": "2026-09-16T20:53:08+08:00",
                "Domain": "test-ai.eo.cn",
                "OwnershipVerification": {
                    "DnsVerification": {
                        "RecordType": "TXT",
                        "RecordValue": "reclaim-4lp50hbpdy0onjdgr01iley749id8kms",
                        "Subdomain": "edgeonereclaim.test-ai"
                    },
                    "FileVerification": {
                        "Content": "4lp50hbpdy0onjdgr01iley749id8kms",
                        "Path": "/.well-known/teo-verification/vaqscx04xy.txt"
                    }
                },
                "Status": "Init",
                "UpdateTime": "2026-09-16T20:53:08+08:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "531d098e-65d0-494e-bf65-d6986ed1e389"
    }
}
```

