**Example 1: 云边界待治理风险列表**



Input: 

```
tccli csip DescribeExposeRisks --cli-unfold-argument  \
    --MemberId mem-tencent-9859c1891731779c \
    --ExposureID 3896
```

Output: 
```
{
    "Response": {
        "ExposeRiskList": [
            {
                "RuleType": "netscan_weakpwd",
                "Severity": "emergency",
                "Title": "u7f51u7edcu626bu63cfu53d1u73b0u5f31u53e3u4ee4"
            }
        ],
        "RequestId": "35605f25-b96d-4ed7-8b09-bd7af5de85eb"
    }
}
```

