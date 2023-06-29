**Example 1: 查询资源信息**



Input: 

```
tccli anicloud QueryResourceInfo --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "Resource": {
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
        },
        "RequestId": "xx"
    }
}
```

