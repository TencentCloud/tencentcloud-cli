**Example 1: 示例**



Input: 

```
tccli cwp DescribeLogDeliveryKafkaOptions --cli-unfold-argument  \
    --InstanceID ckafka-ce80kte5
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "InstanceID": "ckafka-ce80k",
                "InstanceName": "云环境",
                "KafkaVersion": "0.10.2.1",
                "DiskSize": 300,
                "VpcId": "vpc-sdfd***",
                "SubnetId": "subnet-***",
                "Healthy": 1,
                "Zone": "广州三区",
                "Az": "广州",
                "Bandwidth": 320,
                "TopicList": [
                    {
                        "TopicID": "topic-epj9",
                        "TopicName": "bruteforce_attack"
                    },
                    {
                        "TopicID": "topic-r48k",
                        "TopicName": "create_snapshot"
                    }
                ],
                "RouteList": [
                    {
                        "RouteID": 5427,
                        "Domain": "a.yd***",
                        "DomainPort": 0,
                        "Vip": "172.100.100.100:9092",
                        "VipType": 3,
                        "AccessType": 0
                    }
                ]
            }
        ],
        "RequestId": "3758d2c5-57d1-471a-b713-ad353665ce62"
    }
}
```

