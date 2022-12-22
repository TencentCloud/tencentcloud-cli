**Example 1: 查询资源**



Input: 

```
tccli anicloud QueryResource --cli-unfold-argument  \
    --PageNumber 0 \
    --Type 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "RequestId": "xx",
        "Resources": [
            {
                "Status": 0,
                "ExpireTime": "xx",
                "RenewFlag": 0,
                "Key": "xx",
                "AppName": "xx",
                "URL": "xx",
                "ResourceId": "xx",
                "GoodsDetail": {
                    "ProductCode": "xx",
                    "Type": [
                        "xx"
                    ],
                    "GoodsNum": 0,
                    "SubProductCode": "xx"
                },
                "IsolatedTimestamp": "xx",
                "ZoneId": 0,
                "PayMode": 0,
                "Alias": "xx",
                "PackageName": "xx",
                "Region": 0,
                "SdkAppId": "xx",
                "AppId": 0,
                "Entry": "xx",
                "UIN": "xx",
                "CreateTime": "xx",
                "InstType": 0
            }
        ]
    }
}
```

