**Example 1: 获取风险项视角列表**



Input: 

```
tccli csip DescribeRiskItemList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-123456789",
        "Data": [
            {
                "AppId": 123456789,
                "PolicyName": "COS公开访问检测",
                "PolicyId": "policy-001",
                "PolicyType": 1,
                "PolicyRiskLevel": 3,
                "HandleBucketCount": 5,
                "LastScanTimestamp": 1705293000
            },
            {
                "AppId": 123456789,
                "PolicyName": "COS敏感数据检测",
                "PolicyId": "policy-002",
                "PolicyType": 2,
                "PolicyRiskLevel": 4,
                "HandleBucketCount": 3,
                "LastScanTimestamp": 1705296000
            },
            {
                "AppId": 123456789,
                "PolicyName": "COS异常访问检测",
                "PolicyId": "policy-003",
                "PolicyType": 3,
                "PolicyRiskLevel": 2,
                "HandleBucketCount": 8,
                "LastScanTimestamp": 1705299000
            },
            {
                "AppId": 123456789,
                "PolicyName": "COS权限配置检测",
                "PolicyId": "policy-004",
                "PolicyType": 4,
                "PolicyRiskLevel": 3,
                "HandleBucketCount": 2,
                "LastScanTimestamp": 1705302000
            },
            {
                "AppId": 123456789,
                "PolicyName": "COS数据加密检测",
                "PolicyId": "policy-005",
                "PolicyType": 5,
                "PolicyRiskLevel": 2,
                "HandleBucketCount": 6,
                "LastScanTimestamp": 1705305000
            }
        ],
        "Total": 5
    }
}
```

