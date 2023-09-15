**Example 1: 查询购买的预付费商品列表**



Input: 

```
tccli vod DescribePrepaidProducts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ProductInstanceSet": [
            {
                "ProductInstanceId": "50011-251007502-27891",
                "ProductType": "ResourcePackage",
                "StartTime": "2019-02-23T16:00:00Z",
                "ExpireTime": "2020-02-23T16:01:00Z",
                "LastConsumeDate": "2020-02-22T16:00:00Z",
                "BindStatus": 0,
                "ProductInstanceStatus": "Effective",
                "RenewStatus": "Never",
                "ResourceSet": [
                    {
                        "ResourceType": "Review",
                        "Amount": 18000,
                        "Left": 6376
                    }
                ],
                "RefundStatus": "Denied"
            }
        ],
        "RequestId": "requestId"
    }
}
```

