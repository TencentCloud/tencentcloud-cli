**Example 1: 获取Web站点详情**



Input: 

```
tccli cwp DescribeAssetWebLocationInfo --cli-unfold-argument  \
    --Quuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Uuid 24c9be55-c743-4a75-a5c7-2a2912341234 \
    --Id 1024
```

Output: 
```
{
    "Response": {
        "WebLocation": {
            "Name": "test-name",
            "Port": "22",
            "Proto": "tcp",
            "ServiceType": "web",
            "SafeStatus": 1,
            "User": "root",
            "MainPath": "/root",
            "Command": "",
            "Ip": "10.0.0.11",
            "UpdateTime": "2024-10-11 12:23:34"
        },
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

