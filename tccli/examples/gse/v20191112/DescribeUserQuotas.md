**Example 1: 获取用户配额示例**



Input: 

```
tccli gse DescribeUserQuotas --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaResource": [
            {
                "ExtraInfo": "",
                "HardLimit": 20,
                "Remaining": 4,
                "ResourceType": 2
            },
            {
                "ExtraInfo": "",
                "HardLimit": 20,
                "Remaining": 2,
                "ResourceType": 3
            },
            {
                "ExtraInfo": "{\"AssertCapacityQuota\":\"100GB\",\"AssertCapacitySurplus\":\"80GB\"}",
                "HardLimit": 20,
                "Remaining": 10,
                "ResourceType": 1
            },
            {
                "ExtraInfo": "",
                "HardLimit": 20,
                "Remaining": 10,
                "ResourceType": 5
            }
        ],
        "RequestId": "s1585793458903733954",
        "Total": 4
    }
}
```

