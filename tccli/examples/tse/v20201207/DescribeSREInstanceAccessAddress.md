**Example 1: 查询引擎实例访问地址**



Input: 

```
tccli tse DescribeSREInstanceAccessAddress --cli-unfold-argument  \
    --InstanceId sre-12345678
```

Output: 
```
{
    "Response": {
        "EnvAddressInfos": [
            {
                "EnableConfigInternet": true,
                "EnvName": "xx",
                "ConfigIntranetAddress": "xx",
                "ConfigInternetServiceIp": "xx"
            }
        ],
        "LimiterAddressInfos": [
            {
                "IntranetAddress": "xx"
            }
        ],
        "IntranetAddress": "xx",
        "InternetAddress": "xx",
        "ConsoleInternetBandWidth": 0,
        "ConsoleIntranetAddress": "xx",
        "RequestId": "xx",
        "ConsoleInternetAddress": "xx",
        "InternetBandWidth": 0
    }
}
```

