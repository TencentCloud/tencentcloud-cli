**Example 1: 查询通知**



Input: 

```
tccli as DescribeNotificationConfigurations --cli-unfold-argument  \
    --AutoScalingNotificationIds asn-9bhwvxqh
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AutoScalingNotificationSet": [
            {
                "TargetType": "USER_GROUP",
                "TopicName": "topicname",
                "QueueName": "queuename",
                "AutoScalingGroupId": "asg-2umy3jbd",
                "NotificationUserGroupIds": [
                    "1678"
                ],
                "NotificationTypes": [
                    "SCALE_OUT_SUCCESSFUL"
                ],
                "AutoScalingNotificationId": "asn-9bhwvxqh"
            }
        ],
        "RequestId": "0539a5fc-14b8-4591-9fe2-faee32031a64"
    }
}
```

