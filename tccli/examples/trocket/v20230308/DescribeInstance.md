**Example 1: 查询集群信息成功**

查询集群信息成功

Input: 

```
tccli trocket DescribeInstance --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o
```

Output: 
```
{
    "Response": {
        "ScaledTpsEnabled": false,
        "InstanceType": "EXPERIMENT",
        "InstanceId": "rmq-72mo3a9o",
        "InstanceName": "test_instance",
        "TopicNum": 2,
        "TopicNumLimit": 50,
        "GroupNum": 10,
        "GroupNumLimit": 500,
        "MessageRetention": 72,
        "RetentionUpperLimit": 168,
        "RetentionLowerLimit": 1,
        "TpsLimit": 500,
        "ScaledTpsLimit": 0,
        "MaxMessageDelay": 168,
        "CreatedTime": 1731920303801,
        "SendReceiveRatio": 0.5,
        "TagList": [
            {
                "TagKey": "test_tag_key",
                "TagValue": "test_tag_value"
            }
        ],
        "EndpointList": [
            {
                "Type": "VPC",
                "Status": "OPEN",
                "PayMode": "PREPAID",
                "EndpointUrl": "rmq-72mo3a9o.rocketmq.xx.qcloud.tencenttdmq.com:8080",
                "VpcId": "vpc-be1tvrab",
                "SubnetId": "subnet-i6fjswac",
                "Bandwidth": 0,
                "IpRules": []
            }
        ],
        "TopicQueueNumUpperLimit": 32,
        "TopicQueueNumLowerLimit": 1,
        "Remark": "测试集群",
        "InstanceStatus": "RUNNING",
        "SkuCode": "experiment_500",
        "PayMode": "PREPAID",
        "RequestId": "32759095-0372-4ec0-ae3a-e5a2759fd0ff"
    }
}
```

