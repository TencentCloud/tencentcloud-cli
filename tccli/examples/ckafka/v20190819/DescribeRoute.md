**Example 1: 查看路由信息**

查看路由信息

Input: 

```
tccli ckafka DescribeRoute --cli-unfold-argument  \
    --InstanceId xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Routers": [
                {
                    "AccessType": 0,
                    "RouteId": 0,
                    "VipType": 0,
                    "VipList": [
                        {
                            "Vip": "1.1.1.1",
                            "Vport": "8080"
                        }
                    ],
                    "Domain": "abc",
                    "DomainPort": 0,
                    "DeleteTimestamp": "abc",
                    "Subnet": "abc",
                    "BrokerVipList": [
                        {
                            "Vip": "1.1.1.2",
                            "Vport": "90"
                        }
                    ],
                    "VpcId": "vpc-fdafdsa"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

