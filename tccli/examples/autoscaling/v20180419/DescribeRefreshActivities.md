**Example 1: 使用Filters查看刷新活动列表**

使用Filters查询刷新活动 asr-cs0fxpcu。

Input: 

```
tccli as DescribeRefreshActivities --cli-unfold-argument  \
    --Filters.0.Name refresh-activity-id \
    --Filters.0.Values asr-cs0fxpcu
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RefreshActivitySet": [
            {
                "Status": "SUCCESSFUL",
                "RefreshBatchSet": [
                    {
                        "RefreshBatchNum": 3,
                        "EndTime": "2023-09-07T16:32:56Z",
                        "RefreshBatchRelatedInstanceSet": [
                            {
                                "InstanceId": "ins-w188n53l",
                                "InstanceStatusMessage": "success",
                                "LastActivityId": "asa-pb2y1bna",
                                "InstanceStatus": "SUCCESSFUL"
                            }
                        ],
                        "StartTime": "2023-09-07T16:31:44Z",
                        "RefreshBatchStatus": "SUCCESSFUL"
                    },
                    {
                        "RefreshBatchNum": 2,
                        "EndTime": "2023-09-07T16:31:44Z",
                        "RefreshBatchRelatedInstanceSet": [
                            {
                                "InstanceId": "ins-w1824wre",
                                "InstanceStatusMessage": "success",
                                "LastActivityId": "asa-e8dqz8r6",
                                "InstanceStatus": "SUCCESSFUL"
                            },
                            {
                                "InstanceId": "ins-w188n53m",
                                "InstanceStatusMessage": "success",
                                "LastActivityId": "asa-e8dqz8r6",
                                "InstanceStatus": "SUCCESSFUL"
                            }
                        ],
                        "StartTime": "2023-09-07T16:29:56Z",
                        "RefreshBatchStatus": "SUCCESSFUL"
                    },
                    {
                        "RefreshBatchNum": 1,
                        "EndTime": "2023-09-07T16:29:55Z",
                        "RefreshBatchRelatedInstanceSet": [
                            {
                                "InstanceId": "ins-w188n53k",
                                "InstanceStatusMessage": "success",
                                "LastActivityId": "asa-e0o3uxsu",
                                "InstanceStatus": "SUCCESSFUL"
                            },
                            {
                                "InstanceId": "ins-w188n53n",
                                "InstanceStatusMessage": "success",
                                "LastActivityId": "asa-e0o3uxsu",
                                "InstanceStatus": "SUCCESSFUL"
                            }
                        ],
                        "StartTime": "2023-09-07T16:27:49Z",
                        "RefreshBatchStatus": "SUCCESSFUL"
                    }
                ],
                "RefreshMode": "ROLLING_UPDATE_RESET",
                "AutoScalingGroupId": "asg-kgujlegg",
                "ActivityType": "NORMAL",
                "RefreshSettings": {
                    "CheckInstanceTargetHealth": true,
                    "RollingUpdateSettings": {
                        "BatchNumber": 3,
                        "BatchPause": "AUTOMATIC"
                    }
                },
                "OriginRefreshActivityId": "",
                "CurrentRefreshBatchNum": 3,
                "RefreshActivityId": "asr-cs0fxpcu",
                "StartTime": "2023-09-07T16:27:49Z",
                "CreatedTime": "2023-09-07T16:27:49Z",
                "EndTime": "2023-09-07T16:32:56Z"
            }
        ],
        "RequestId": "48869660-f1df-4085-a62c-1f9636cbe030"
    }
}
```

