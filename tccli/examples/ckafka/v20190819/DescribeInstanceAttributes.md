**Example 1: 获取实例属性**



Input: 

```
tccli ckafka DescribeInstanceAttributes --cli-unfold-argument  \
    --InstanceId xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Tags": [],
            "InstanceId": "instance-will-s",
            "InstanceName": "treTest",
            "VipList": [
                {
                    "Vip": "172.16.16.135",
                    "Vport": "9092"
                }
            ],
            "Vip": "172.16.16.135",
            "Vport": "9092",
            "Status": 1,
            "Bandwidth": 48000,
            "DiskSize": 120000,
            "ZoneId": 100003,
            "VpcId": "vpc-1qkosjcb",
            "SubnetId": "subnet-lt4shnme",
            "Healthy": 1,
            "HealthyMessage": "连接数:0#磁盘使用百分比:0%#消费峰值带宽0MB/s",
            "CreateTime": "1970-01-19 06:46:02",
            "MsgRetentionTime": "1970-01-01 08:00:05",
            "Config": {
                "AutoCreateTopicsEnable": true,
                "NumPartitions": 3,
                "DefaultReplicationFactor": 2
            },
            "RemainderPartitions": 45,
            "RemainderTopics": 17,
            "CreatedPartitions": 0,
            "CreatedTopics": 0
        },
        "RequestId": "33a2224e-156d-4f23-9ffe-3c66d545c59c"
    }
}
```

