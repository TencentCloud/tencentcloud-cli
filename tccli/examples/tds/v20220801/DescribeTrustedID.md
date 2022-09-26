**Example 1: 查询设备标识**



Input: 

```
tccli tds DescribeTrustedID --cli-unfold-argument  \
    --DeviceToken xx
```

Output: 
```
{
    "Response": {
        "Openid": "xx",
        "Brand": "xx",
        "SdkBuildNo": "xx",
        "AppVersion": "xx",
        "Platform": "xx",
        "SystemVersion": "xx",
        "RequestId": "xx",
        "NetworkType": "xx",
        "Model": "xx",
        "PackageName": "xx",
        "ClientIp": "xx"
    }
}
```

