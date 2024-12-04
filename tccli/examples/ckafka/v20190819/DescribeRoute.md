**Example 1: 查看路由信息**

查看路由信息

Input: 

```
tccli ckafka DescribeRoute --cli-unfold-argument  \
    --InstanceId ckafka-na37x9qa
```

Output: 
```
{
    "Response": {
        "RequestId": "972ab361-b677-4431-9f49-f54f8e1e62ab",
        "Result": {
            "Routers": [
                {
                    "AccessType": 0,
                    "BrokerVipList": [
                        {
                            "Vip": "11.135.14.76",
                            "Vport": "7609"
                        },
                        {
                            "Vip": "11.135.14.76",
                            "Vport": "7610"
                        },
                        {
                            "Vip": "11.135.14.76",
                            "Vport": "7611"
                        }
                    ],
                    "DeleteTimestamp": "",
                    "Domain": "",
                    "DomainPort": 0,
                    "RouteId": 136207,
                    "Subnet": "subnet-m7o87b20",
                    "VipList": [
                        {
                            "Vip": "11.135.14.76",
                            "Vport": "7608"
                        }
                    ],
                    "VipType": 7,
                    "VpcId": "vpc-n3n50e5r"
                },
                {
                    "AccessType": 0,
                    "BrokerVipList": [
                        {
                            "Vip": "10.0.0.15",
                            "Vport": "9093"
                        },
                        {
                            "Vip": "10.0.0.15",
                            "Vport": "9094"
                        },
                        {
                            "Vip": "10.0.0.15",
                            "Vport": "9095"
                        }
                    ],
                    "DeleteTimestamp": "",
                    "Domain": "",
                    "DomainPort": 0,
                    "RouteId": 137005,
                    "Subnet": "subnet-pu55o55e",
                    "VipList": [
                        {
                            "Vip": "10.0.0.15",
                            "Vport": "9092"
                        }
                    ],
                    "VipType": 3,
                    "VpcId": "vpc-ktradax5"
                },
                {
                    "AccessType": 1,
                    "BrokerVipList": [
                        {
                            "Vip": "106.55.222.195",
                            "Vport": "50009"
                        },
                        {
                            "Vip": "106.55.222.195",
                            "Vport": "50010"
                        },
                        {
                            "Vip": "106.55.222.195",
                            "Vport": "50011"
                        }
                    ],
                    "DeleteTimestamp": "",
                    "Domain": "ckafka-na37x9qa.ap-guangzhou.ckafka.tencentcloudmq.com",
                    "DomainPort": 50000,
                    "RouteId": 137270,
                    "Subnet": "",
                    "VipList": [
                        {
                            "Vip": "81.71.20.57",
                            "Vport": "50000"
                        }
                    ],
                    "VipType": 1,
                    "VpcId": "vpc-ks7w9y0b"
                },
                {
                    "AccessType": 0,
                    "BrokerVipList": [
                        {
                            "Vip": "11.135.14.109",
                            "Vport": "8281"
                        },
                        {
                            "Vip": "11.135.14.109",
                            "Vport": "8282"
                        },
                        {
                            "Vip": "11.135.14.109",
                            "Vport": "8283"
                        }
                    ],
                    "DeleteTimestamp": "",
                    "Domain": "",
                    "DomainPort": 0,
                    "RouteId": 137606,
                    "Subnet": "subnet-m7o87b20",
                    "VipList": [
                        {
                            "Vip": "11.135.14.109",
                            "Vport": "8280"
                        }
                    ],
                    "VipType": 7,
                    "VpcId": "vpc-n3n50e5r"
                }
            ]
        }
    }
}
```

