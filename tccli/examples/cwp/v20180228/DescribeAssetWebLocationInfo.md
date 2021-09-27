**Example 1: 获取Web站点详情**



Input: 

```
tccli cwp DescribeAssetWebLocationInfo --cli-unfold-argument  \
    --Quuid xx \
    --Uuid xx \
    --Id xx
```

Output: 
```
{
    "Response": {
        "WebLocation": {
            "ServiceType": "xx",
            "Name": "xx",
            "SafeStatus": 1,
            "Ip": "xx",
            "Proto": "xx",
            "MainPath": "xx",
            "Command": "xx",
            "User": "xx",
            "Port": 1
        },
        "RequestId": "xx"
    }
}
```

