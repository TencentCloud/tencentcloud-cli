**Example 1: 查询服务列表状态**

查询服务列表状态

Input: 

```
tccli apigateway DescribeServicesStatus --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "ServiceSet": [
                {
                    "InnerHttpsPort": 0,
                    "ServiceDesc": "abc",
                    "Protocol": "abc",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "NetTypes": [
                        "abc"
                    ],
                    "ExclusiveSetName": "abc",
                    "ServiceId": "abc",
                    "IpVersion": "abc",
                    "AvailableEnvironments": [
                        "abc"
                    ],
                    "ServiceName": "abc",
                    "OuterSubDomain": "abc",
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "InnerHttpPort": 1,
                    "InnerSubDomain": "abc",
                    "TradeIsolateStatus": 0,
                    "Tags": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ],
                    "InstanceId": "abc",
                    "SetType": "abc",
                    "DeploymentType": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

