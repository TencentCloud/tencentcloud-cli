**Example 1: 获取kafka投递信息**



Input: 

```
tccli cwp DescribeLogKafkaDeliverInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessAddr": "100.119.167.50:6281",
        "AccessType": 2,
        "Az": "广州三区",
        "BandWidth": 0,
        "DeliverStatus": 1,
        "DeliverTypeDetails": [
            {
                "SecurityType": 1,
                "LogType": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "TopicId": "topic-p9d8q5tm",
                "TopicName": "test",
                "Switch": 1,
                "Status": 0,
                "ErrInfo": " "
            }
        ],
        "DiskSize": 0,
        "InsVersion": "0.10.2.1",
        "KafkaEnvName": "云镜测试环境",
        "KafkaId": "ckafka-ce80kte5",
        "RequestId": "33e0611b-d363-4727-a7d6-ca405225bd52",
        "SubnetId": "-",
        "Username": "yunjing2",
        "VpcId": "-",
        "Zone": "广州"
    }
}
```

