**Example 1: 查询 ACL 告警列表示例**



Input: 

```
tccli csip DescribeSandboxACLAlertList --cli-unfold-argument  \
    --Filters.0.Name Status \
    --Filters.0.Values PENDING
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 7001,
                "BelongAssetType": "HOST",
                "RuleID": 2001,
                "RuleName": "禁止出站访问未知域名",
                "UUID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                "InstanceId": "ins-a1b2c3d4",
                "InstanceName": "app-server-01",
                "Exe": "/usr/bin/curl",
                "Param": "curl -X GET https://evil.example.com/c2",
                "Target": "GET https://evil.example.com/c2",
                "Protocol": "https",
                "Level": "HIGH",
                "Status": "PENDING",
                "Count": 12,
                "FirstAlertTime": "2025-03-10T08:00:00+08:00",
                "LastAlertTime": "2025-03-15T14:30:00+08:00",
                "RuleAction": "BLOCK"
            }
        ],
        "TotalCount": 42,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

