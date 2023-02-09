**Example 1: 查询引擎实例访问地址**

查询引擎实例CLB服务访问地址

Input: 

```
tccli tse DescribeEngineClbAccessAddress --cli-unfold-argument  \
    --InstanceId sre-12345678
```

Output: 
```
{
    "Response": {
        "ReportIntranetAddress": "xx",
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
        "ConsoleIntranetAddress": "xx",
        "ClientIntranetAddress": "xx",
        "EnableClientIntranet": true,
        "RequestId": "xx"
    }
}
```

