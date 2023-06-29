**Example 1: 查询安全日志投递kafka可选项**



Input: 

```
tccli tcss DescribeSecLogDeliveryKafkaOptions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "InstanceID": "xx",
                "TopicList": [
                    {
                        "TopicID": "xx",
                        "TopicName": "xx"
                    }
                ],
                "RouteList": [
                    {
                        "Domain": "xx",
                        "AccessType": 0,
                        "RouteID": 0,
                        "Vip": "xx",
                        "DomainPort": 1,
                        "VipType": 0
                    }
                ],
                "InstanceName": "xx"
            }
        ],
        "RegionList": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州"
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

