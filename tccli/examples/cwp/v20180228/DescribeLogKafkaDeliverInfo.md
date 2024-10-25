**Example 1: 获取kafka投递信息**



Input: 

```
tccli cwp DescribeLogKafkaDeliverInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "KafkaEnvName": "name",
        "KafkaId": "ckafka-xxx",
        "Zone": "10006",
        "Az": "az",
        "VpcId": "vpc-xxx",
        "SubnetId": "subnet-xxx",
        "AccessType": 1,
        "AccessAddr": "addr",
        "DeliverStatus": 1,
        "InsVersion": "1.0.1",
        "BandWidth": 0,
        "DiskSize": 0,
        "Username": "username",
        "DeliverTypeDetails": [
            {
                "SecurityType": 1,
                "LogType": [
                    0
                ],
                "TopicId": "topic-xxx",
                "TopicName": "topic-name",
                "Switch": 1,
                "Status": 1,
                "ErrInfo": "err",
                "StatusTime": 0,
                "LogName": "log-name",
                "LogSetId": "cls-xxx",
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

