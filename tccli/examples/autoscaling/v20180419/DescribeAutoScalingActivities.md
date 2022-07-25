**Example 1: 使用Filters查看伸缩活动列表**



Input: 

```
tccli as DescribeAutoScalingActivities --cli-unfold-argument  \
    --Filters.0.Values asa-o4v87ae9 \
    --Filters.0.Name activity-id
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ActivitySet": [
            {
                "Description": "Activity was launched in response to a difference between desired capacity and actual capacity, scale out 1 instance(s).",
                "AutoScalingGroupId": "asg-2umy3jbd",
                "ActivityRelatedInstanceSet": [
                    {
                        "InstanceId": "ins-q3ss14yo",
                        "InstanceStatus": "SUCCESSFUL"
                    }
                ],
                "LifecycleActionResultSet": [],
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

**Example 2: 根据伸缩活动ID查询伸缩活动列表**



Input: 

```
tccli as DescribeAutoScalingActivities --cli-unfold-argument  \
    --ActivityIds asa-o4v87ae9
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ActivitySet": [
            {
                "Description": "Activity was launched in response to a difference between desired capacity and actual capacity, scale out 1 instance(s).",
                "AutoScalingGroupId": "asg-2umy3jbd",
                "ActivityRelatedInstanceSet": [
                    {
                        "InstanceId": "ins-q3ss14yo",
                        "InstanceStatus": "SUCCESSFUL"
                    }
                ],
                "LifecycleActionResultSet": [],
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

