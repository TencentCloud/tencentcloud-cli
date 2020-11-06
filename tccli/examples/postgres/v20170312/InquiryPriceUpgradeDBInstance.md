**Example 1: Query prices of upgrading DB instances**



Input: 

```
tccli postgres InquiryPriceUpgradeDBInstance --cli-unfold-argument  \
    --DBInstanceId postgres-6fego161 \
    --Memory 4 \
    --Storage 500
```

Output: 
```
{
    "Response": {
        "Price": 1300,
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "OriginalPrice": 1300
    }
}
```

