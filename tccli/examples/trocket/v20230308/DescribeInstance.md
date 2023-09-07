**Example 1: 查询实例**

查询实例

Input: 

```
tccli trocket DescribeInstance --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "InstanceType": "abc",
        "InstanceId": "abc",
        "InstanceName": "abc",
        "TopicNum": 0,
        "TopicNumLimit": 0,
        "GroupNum": 0,
        "GroupNumLimit": 0,
        "MessageRetention": 0,
        "RetentionUpperLimit": 0,
        "RetentionLowerLimit": 0,
        "TpsLimit": 0,
        "ScaledTpsLimit": 0,
        "MaxMessageDelay": 0,
        "CreatedTime": 0,
        "SendReceiveRatio": 0,
        "TagList": [
            {
                "TagKey": "abc",
                "TagValue": "abc"
            }
        ],
        "EndpointList": [
            {
                "Type": "abc",
                "Status": "abc",
                "PayMode": "abc",
                "EndpointUrl": "abc",
                "VpcId": "abc",
                "SubnetId": "abc",
                "Bandwidth": 0,
                "IpRules": [
                    {
                        "Ip": "abc",
                        "Allow": true,
                        "Remark": "abc"
                    }
                ]
            }
        ],
        "TopicQueueNumUpperLimit": 0,
        "TopicQueueNumLowerLimit": 0,
        "Remark": "abc",
        "InstanceStatus": "abc",
        "SkuCode": "abc",
        "PayMode": "abc",
        "RequestId": "abc"
    }
}
```

