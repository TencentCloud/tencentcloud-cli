**Example 1: 查询路由健康状态**



Input: 

```
tccli vpc DescribeServiceStateInternal --cli-unfold-argument  \
    --GetServiceStateSet.0.VpcId 1 \
    --GetServiceStateSet.0.Protocol tcp \
    --GetServiceStateSet.0.HostIp 1.1.1.1 \
    --GetServiceStateSet.0.State 1 \
    --GetServiceStateSet.0.Vip 10.6.2.3 \
    --GetServiceStateSet.0.VirtualPort 8181 \
    --GetServiceStateSet.0.UniqueVpcId vpc-jmaywf6r \
    --GetServiceStateSet.0.GroupId 1
```

Output: 
```
{
    "Response": {
        "GetServiceStateResult": [
            {
                "VpcId": 80509,
                "Protocol": "tcp",
                "State": [
                    {
                        "ServiceInfo": "Tcp:11.145.98.76:80",
                        "State": 0
                    }
                ],
                "Vip": "10.3.153.1",
                "VirtualPort": 80,
                "GroupId": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

