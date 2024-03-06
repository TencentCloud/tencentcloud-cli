**Example 1: 获取kafka投递信息**



Input: 

```
tccli cwp DescribeLogKafkaDeliverInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "KafkaEnvName": "abc",
        "KafkaId": "abc",
        "Zone": "abc",
        "Az": "abc",
        "VpcId": "abc",
        "SubnetId": "abc",
        "AccessType": 1,
        "AccessAddr": "abc",
        "DeliverStatus": 1,
        "InsVersion": "abc",
        "BandWidth": 0,
        "DiskSize": 0,
        "Username": "abc",
        "DeliverTypeDetails": [
            {
                "SecurityType": 1,
                "LogType": [
                    0
                ],
                "TopicId": "abc",
                "TopicName": "abc",
                "Switch": 1,
                "Status": 1,
                "ErrInfo": "abc",
                "StatusTime": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

