**Example 1: 示例**



Input: 

```
tccli cwp DescribeLicenseList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "de41ce31-f2c0-49a9-a476-57051a5c7c6c",
        "TotalCount": 1,
        "List": [
            {
                "LicenseId": 1,
                "LicenseType": 0,
                "LicenseStatus": 0,
                "LicenseCnt": 0,
                "UsedLicenseCnt": 0,
                "OrderStatus": 1,
                "BuyTime": "2018-02-28 00:00:00",
                "Deadline": "2018-02-28 00:00:00",
                "ResourceId": "1c007adc2f0bb9f7c052860e2d3703fa",
                "AutoRenewFlag": 0,
                "ProjectId": 1,
                "TaskId": 1,
                "SourceType": 0,
                "Alias": "资源别名",
                "Tags": [
                    {
                        "TagKey": "标签键",
                        "TagValue": "标签值"
                    }
                ]
            }
        ]
    }
}
```

