**Example 1: 查询终端节点组**



Input: 

```
tccli ga2 DescribeEndpointGroups --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka
```

Output: 
```
{
    "Response": {
        "EndpointGroupConfigurationSet": [
            {
                "GlobalAcceleratorId": "ga-80d9rt60",
                "ListenerId": "lsr-d5u7fac7",
                "EndpointGroupId": "epg-3j2j37kw",
                "Name": "sasac",
                "EndpointGroupRegion": "ap-beijing",
                "Description": "",
                "EndpointGroupType": "DEFAULT",
                "EnableHealthCheck": false,
                "ConnectTimeout": 2,
                "HealthCheckInterval": 30,
                "UnhealthyThreshold": 3,
                "HealthyThreshold": 3,
                "CheckType": "",
                "CheckPort": 0,
                "ContextType": "",
                "CheckSendContext": "",
                "CheckRecvContext": "",
                "ForwardProtocol": "HTTPS",
                "CheckDomain": "",
                "CheckPath": "",
                "CheckMethod": "",
                "OriginPublicIps": [
                    "49.233.210.240",
                    "82.156.37.248",
                    "49.233.108.234",
                    "81.70.235.113",
                    "101.42.53.111",
                    "49.233.248.15",
                    "101.43.214.93",
                    "152.136.226.86",
                    "81.70.101.190",
                    "62.234.94.120",
                    "152.136.97.154",
                    "43.138.28.144",
                    "62.234.163.16",
                    "62.234.146.108",
                    "82.156.101.252",
                    "152.136.156.197",
                    "62.234.138.210",
                    "101.43.140.145",
                    "42.193.118.160",
                    "49.233.85.107"
                ],
                "StatusMask": [],
                "PortOverrides": [
                    {
                        "ListenerPort": 56413,
                        "EndpointPort": 26
                    }
                ],
                "VirtualExistForwardingRuleFlag": false,
                "EndpointConfigurations": [
                    {
                        "EndpointType": "CustomDomain",
                        "EndpointService": "www.qq.com",
                        "Weight": 100,
                        "HealthCheckStatus": ""
                    }
                ]
            }
        ],
        "TotalCount": 12,
        "RequestId": "7a848272-260f-46f6-965e-5d4b7b31eb85"
    }
}
```

