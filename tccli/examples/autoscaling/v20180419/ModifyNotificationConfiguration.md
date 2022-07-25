**Example 1: 修改事件通知**



Input: 

```
tccli as ModifyNotificationConfiguration --cli-unfold-argument  \
    --NotificationUserGroupIds 1678 \
    --NotificationTypes SCALE_IN_FAILED SCALE_IN_SUCCESSFUL \
    --AutoScalingNotificationId asn-2sestqbr
```

Output: 
```
{
    "Response": {
        "RequestId": "52e32a5b-5f69-4d48-a3f1-f2fea5c43a70"
    }
}
```

