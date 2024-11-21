**Example 1: 获取kafka投递信息**



Input: 

```
tccli cwp DescribeLogKafkaDeliverInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "KafkaEnvName": "name",
        "KafkaId": "ckafka-sfs",
        "Zone": "10006",
        "Az": "az",
        "VpcId": "vpc-fdfs",
        "SubnetId": "subnet-fdfd",
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
                "TopicId": "topic-dad",
                "TopicName": "topic-name",
                "Switch": 1,
                "Status": 1,
                "ErrInfo": "err",
                "StatusTime": 0,
                "LogName": "log-name",
                "LogSetId": "cls-wfd",
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "acdd5474-6360-4fd4-bfc7-843162cb8116"
    }
}
```

