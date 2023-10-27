**Example 1: 查询所有检查项示例**



Input: 

```
tccli tcss DescribeCheckItemList --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ClusterCheckItems": [
            {
                "CheckItemId": 0,
                "Name": "abc",
                "ItemDetail": "abc",
                "RiskLevel": "abc",
                "RiskTarget": "abc",
                "RiskType": "abc",
                "RiskAttribute": "abc",
                "RiskProperty": "abc",
                "CVENumber": "abc",
                "DiscoverTime": "abc",
                "Solution": "abc",
                "CVSS": "abc",
                "CVSSScore": "abc",
                "RelateLink": "abc",
                "AffectedType": "abc",
                "AffectedVersion": "abc",
                "IgnoredAssetNum": 0,
                "IsIgnored": true,
                "RiskAssessment": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

