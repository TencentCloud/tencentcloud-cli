**Example 1: 查询计算环境的活动列表**



Input: 

```
tccli batch DescribeComputeEnvActivities --cli-unfold-argument  \
    --EnvId env-lcpcej85
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ActivitySet": [
            {
                "ComputeNodeId": "node-9yzd5jei",
                "EnvId": "env-lcpcej85",
                "InstanceId": "ins-x23sd8xk",
                "ActivityState": "SUCCEED",
                "ActivityId": "act-83xvnt5p",
                "StartTime": "2018-03-09T13:14:34Z",
                "StateReason": "",
                "EndTime": "2018-03-09T13:15:44Z",
                "Cause": "ModifyComputeEnv: increase the capacity from 1 to 2",
                "ComputeNodeActivityType": "CREATE_COMPUTE_NODE"
            },
            {
                "ComputeNodeId": "node-noa8vefu",
                "EnvId": "env-lcpcej85",
                "InstanceId": "ins-x23sdiwd",
                "ActivityState": "SUCCEED",
                "ActivityId": "act-ezle9e7v",
                "StartTime": "2018-03-08T11:48:43Z",
                "StateReason": "",
                "EndTime": "2018-03-08T11:49:17Z",
                "Cause": "CreateComputeEnv: the capacity is 1",
                "ComputeNodeActivityType": "CREATE_COMPUTE_NODE"
            }
        ],
        "RequestId": "ecfeec77-6ec1-4daf-8730-1dd00c742252"
    }
}
```

