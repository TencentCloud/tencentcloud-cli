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
        "IntranetAddress": "abc",
        "InternetAddress": "abc",
        "EnvAddressInfos": [
            {
                "EnvName": "abc",
                "EnableConfigInternet": true,
                "ConfigInternetServiceIp": "abc",
                "ConfigIntranetAddress": "abc",
                "EnableConfigIntranet": true,
                "InternetBandWidth": 0
            }
        ],
        "ConsoleInternetAddress": "abc",
        "ConsoleIntranetAddress": "abc",
        "InternetBandWidth": 0,
        "ConsoleInternetBandWidth": 0,
        "LimiterAddressInfos": [
            {
                "IntranetAddress": "abc"
            }
        ],
        "CLBMultiRegion": {
            "CLBMultiZoneFlag": true,
            "CLBMasterZone": "abc",
            "CLBSlaveZone": "abc"
        },
        "RequestId": "abc"
    }
}
```

