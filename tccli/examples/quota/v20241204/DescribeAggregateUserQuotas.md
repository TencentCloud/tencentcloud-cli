**Example 1: 示例1**



Input: 

```
tccli quota DescribeAggregateUserQuotas --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Count": 1,
        "Data": [
            {
                "ApplyType": 1,
                "MemberName": "",
                "MemberUin": 88888888888,
                "ProductName": "Your Product Name",
                "QuotaDescription": "Quota Desc",
                "QuotaDimensions": [
                    {
                        "DimensionName": "Dimension 1",
                        "PrimaryValue": "value 1"
                    },
                    {
                        "DimensionName": "Dimension 2",
                        "PrimaryValue": "value 2"
                    }
                ],
                "QuotaId": 9999,
                "QuotaInstanceId": "",
                "QuotaName": "quota name",
                "QuotaUnit": "GB",
                "TotalQuota": 15,
                "TotalUsage": 0
            }
        ],
        "OwnerUin": 88888888888,
        "RequestId": "b351f392-eddd-42f5-ad53-xxxxxxxx"
    }
}
```

