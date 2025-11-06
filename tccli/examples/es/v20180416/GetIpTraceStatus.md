**Example 1: 查询IP溯源状态**



Input: 

```
tccli es GetIpTraceStatus --cli-unfold-argument  \
    --InstanceId es-xasddassd
```

Output: 
```
{
    "Response": {
        "OpenIpTrace": false,
        "FilterKibanaIp": false,
        "DurationTime": 0,
        "IpTraceConfig": {
            "EnableRequest": false,
            "EnableResponse": false,
            "EnableRequestBody": false,
            "EnableResponseBody": false,
            "RemoteIpInclude": [
                ""
            ],
            "RemoteIpExclude": [
                ""
            ],
            "UriInclude": [
                ""
            ],
            "UriExclude": [
                ""
            ]
        },
        "LastStartTime": "2020-12-28 14:37:36",
        "LastEndTime": "2020-12-28 14:37:36",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

