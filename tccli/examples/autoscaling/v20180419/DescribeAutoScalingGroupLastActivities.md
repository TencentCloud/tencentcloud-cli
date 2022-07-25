**Example 1: 查询伸缩组最新一次伸缩活动列表**



Input: 

```
tccli as DescribeAutoScalingGroupLastActivities --cli-unfold-argument  \
    --AutoScalingGroupIds asg-2umy3jbd
```

Output: 
```
{
    "Response": {
        "ActivitySet": [
            {
                "Description": "Activity was launched in response to a difference between desired capacity and actual capacity, scale out 1 instance(s).",
                "AutoScalingGroupId": "asg-2umy3jbd",
                "LifecycleActionResultSet": [],
                "ActivityRelatedInstanceSet": [
                    {
                        "InstanceId": "ins-q3ss14yo",
                        "InstanceStatus": "SUCCESSFUL"
                    }
                ],
                "DetailedStatusMessageSet": [],
                "ActivityType": "SCALE_OUT",
                "ActivityId": "asa-o4v87ae9",
                "StartTime": "2018-11-20T08:33:56Z",
                "CreatedTime": "2018-11-20T08:33:56Z",
                "EndTime": "2018-11-20T08:34:52Z",
                "Cause": "Activity was launched in response to a difference between desired capacity and actual capacity.",
                "StatusMessageSimplified": "Success",
                "StatusMessage": "Success",
                "StatusCode": "SUCCESSFUL",
                "InvocationResultSet": []
            }
        ],
        "RequestId": "1082ab5d-c985-4d8c-bb9d-0d05e282b4a7"
    }
}
```

