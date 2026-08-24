**Example 1: DescribeLogTypeConfigList**



Input: 

```
tccli csip DescribeDspmLogTypeConfigList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "VipType": 1,
                "InstanceId": "ckafka-istestid",
                "InstanceName": "测试 Ckafka",
                "Vip": "1.1.1.1",
                "Vport": "9092",
                "Domain": "ckafka-istestid.ap-guangzhou.ckafka.tencentcloudmq.com",
                "DomainPort": "9092",
                "RegionId": "ap-guangzhou",
                "VpcId": "vpc-istestid",
                "SubnetId": "subnet-istestid",
                "Healthy": 1,
                "LogType": 1,
                "TopicId": "topic-istestid",
                "TopicName": "alarm_topic",
                "Status": 1,
                "StatusMessages": "success",
                "IsOpen": 1
            }
        ],
        "TotalCount": 0,
        "RequestId": "b0b75456-b364-4935-abf3-9c83dfbd7b4c"
    }
}
```

