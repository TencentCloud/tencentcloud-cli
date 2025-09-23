**Example 1: 获取邮箱泄露数据**



Input: 

```
tccli ctem DescribeLeakageEmails --cli-unfold-argument  \
    --CreateAtEnd 2023-02-01 12:00:00 \
    --CreateAtStart 2023-01-01 12:00:00 \
    --CustomerId 1 \
    --EnterpriseUidList string \
    --Filters.0.Name string \
    --Filters.0.Values string \
    --Format json \
    --Ignored False \
    --IsNew False \
    --Limit 10 \
    --Offset 0 \
    --UpdateAtEnd 2023-02-01 12:00:00 \
    --UpdateAtStart 2023-01-01 12:00:00
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Username": "string",
                "HandlingStatus": 0,
                "Id": 0,
                "Keyword": "string",
                "Email": "string",
                "Remark": "string",
                "RiskLevel": 0,
                "Source": "string",
                "Suggestion": "string"
            }
        ],
        "Total": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

