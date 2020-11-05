**Example 1: Creating notifications for successful and failed scale-out events**



Input: 

```
tccli as CreateNotificationConfiguration --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s\
    --NotificationTypes SCALE_OUT_SUCCESSFUL SCALE_OUT_FAILED\
    --NotificationUserGroupIds 1678
```

Output: 
```
{
    "Response": {
        "AutoScalingNotificationId": "asn-2sestqbr",
        "RequestId": "fb02c8bd-5f38-4786-91b6-0c6e06a88832"
    }
}
```

