**Example 1: 用于查询服务列表**



Input: 

```
tccli apigateway DescribeServicesStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ServiceSet": [
                {
                    "ServiceId": "service-hrxy5qsm",
                    "ServiceName": "ddd",
                    "ServiceDesc": "",
                    "Protocol": "http",
                    "OuterSubDomain": "service-hrxy5qsm-1259027407.gz.apigw.tencentcs.com",
                    "InnerSubDomain": "",
                    "InnerHttpPort": 0,
                    "InnerHttpsPort": 0,
                    "CreatedTime": "2020-03-25T15:24:17Z",
                    "ModifiedTime": "2020-03-25T15:24:18Z",
                    "NetTypes": [
                        "OUTER"
                    ],
                    "IpVersion": "IPv4",
                    "ExclusiveSetName": "",
                    "AvailableEnvironments": [
                        "release"
                    ],
                    "TradeIsolateStatus": 0
                }
            ]
        },
        "RequestId": "7100a7b7-30ed-43c8-8d53-081afb6ecd8b"
    }
}
```

