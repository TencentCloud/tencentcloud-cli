**Example 1: 查询用户所有实例的详细信息**

查询用户所有实例的详细信息

Input: 

```
tccli waf DescribeDomains --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20 \
    --Filters.0.Name Edition \
    --Filters.0.Values sparta_waf \
    --Filters.0.ExactMatch True \
    --Filters.1.Name InstanceId \
    --Filters.1.Values waf_000000002 \
    --Filters.1.ExactMatch True
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Domains": [
            {
                "Domain": "abc",
                "DomainId": "abc",
                "InstanceId": "abc",
                "Cname": "abc",
                "Edition": "abc",
                "Region": "abc",
                "InstanceName": "abc",
                "ClsStatus": 1,
                "FlowMode": 1,
                "Status": 1,
                "Mode": 1,
                "Engine": 1,
                "CCList": [
                    "abc"
                ],
                "RsList": [
                    "abc"
                ],
                "Ports": [
                    {
                        "NginxServerId": 1,
                        "Port": "abc",
                        "Protocol": "abc",
                        "UpstreamPort": "abc",
                        "UpstreamProtocol": "abc"
                    }
                ],
                "LoadBalancerSet": [
                    {
                        "ListenerId": "abc",
                        "ListenerName": "abc",
                        "LoadBalancerId": "abc",
                        "LoadBalancerName": "abc",
                        "Protocol": "abc",
                        "Region": "abc",
                        "Vip": "abc",
                        "Vport": 1,
                        "Zone": "abc",
                        "NumericalVpcId": 0,
                        "LoadBalancerType": "abc"
                    }
                ],
                "AppId": 1,
                "State": 0,
                "CreateTime": "abc",
                "Ipv6Status": 0,
                "BotStatus": 0,
                "Level": 0,
                "PostCLSStatus": 0,
                "PostCKafkaStatus": 0,
                "CdcClusters": "abc",
                "ApiStatus": 0,
                "AlbType": "abc",
                "SgState": 0,
                "SgDetail": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

