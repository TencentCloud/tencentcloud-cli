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
        "IntranetAddress": "10.0.0.1",
        "InternetAddress": "10.0.0.1",
        "EnvAddressInfos": [
            {
                "EnvName": "dev",
                "EnableConfigInternet": true,
                "ConfigInternetServiceIp": "10.0.0.1",
                "ConfigIntranetAddress": "10.0.0.2",
                "EnableConfigIntranet": true,
                "InternetBandWidth": 0
            }
        ],
        "ConsoleInternetAddress": "10.0.0.1",
        "ConsoleIntranetAddress": "10.0.0.2",
        "InternetBandWidth": 0,
        "ConsoleInternetBandWidth": 0,
        "LimiterAddressInfos": [
            {
                "IntranetAddress": "10.0.0.1"
            }
        ],
        "CLBMultiRegion": {
            "CLBMultiZoneFlag": true,
            "CLBMasterZone": "ap-guangzhou-1",
            "CLBSlaveZone": "ap-guangzhou-2"
        },
        "RequestId": "req-id"
    }
}
```

