**Example 1: Modifying an event notification**



Input: 

```
tccli as ModifyNotificationConfiguration --cli-unfold-argument  \
    --AutoScalingNotificationId asn-2sestqbr\
    --NotificationTypes SCALE_IN_SUCCESSFUL SCALE_IN_FAILED\
    --NotificationUserGroupIds 1678
```

Output: 
```
{
    "Response": {
        "RequestId": "52e32a5b-5f69-4d48-a3f1-f2fea5c43a70"
    }
}
```

