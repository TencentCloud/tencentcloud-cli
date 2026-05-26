**Example 1: 获取策略列表信息**



Input: 

```
tccli csip DescribeCosPolicy --cli-unfold-argument  \
    --Filter.Filters.0.Name PolicyName \
    --Filter.Filters.0.Values bucket-*-policy \
    --Filter.Filters.0.OperatorType 9 \
    --Filter.Filters.1.Name PolicyType \
    --Filter.Filters.1.Values 1 2 \
    --Filter.Filters.1.OperatorType 7 \
    --Filter.Filters.2.Name PolicySource \
    --Filter.Filters.2.Values system \
    --Filter.Filters.2.OperatorType 1 \
    --Filter.Filters.3.Name PolicyStatus \
    --Filter.Filters.3.Values 1 \
    --Filter.Filters.3.OperatorType 1 \
    --Filter.Offset 0 \
    --Filter.Limit 20 \
    --Filter.Order desc \
    --Filter.By PolicyName \
    --Filter.StartTime 2024-01-01 00:00:00 \
    --Filter.EndTime 2024-01-31 23:59:59
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "PolicyId": 1,
                "PolicyName": "bucket-public-read-policy",
                "PolicyType": 1,
                "PolicyContent": "{\"Version\":\"2.0\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"qcs\":[\"qcs::cam::anyone:anyone\"]},\"Action\":[\"cos:GetObject\"],\"Resource\":[\"qcs::cos:ap-guangzhou:uid/100012345678:bucket-001/*\"]}]}",
                "PolicyStatus": 1,
                "PolicyDescription": "",
                "PolicyAbnormalType": 1,
                "RiskLevel": 1,
                "PolicySource": 1,
                "PolicyHitCount": 10,
                "PolicyCreateTime": 173147231,
                "PolicyUpdateTime": 173147231,
                "PolicyContentHash": "529fd413763fdcc00e2dae6c55c0a0fe",
                "RelAccountCount": 10,
                "RelAccountUin": "",
                "RelAccountName": ""
            }
        ],
        "Total": 156,
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

