**Example 1: DescribeInstancesByExecutors异常示例**

DescribeInstancesByExecutors异常示例

Input: 

```
tccli wedata DescribeInstancesByExecutors --cli-unfold-argument  \
    --ProjectId  \
    --ExecutorGroupIdList 
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "01ce3409-6f5c-4245-ad76-9f04e05241ec"
    }
}
```

**Example 2: DescribeInstancesByExecutors正常示例**

DescribeInstancesByExecutors正常示例

Input: 

```
tccli wedata DescribeInstancesByExecutors --cli-unfold-argument  \
    --ProjectId 3327414454951170048 \
    --ExecutorGroupIdList 20260107105230846836
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ExecutorGroupId": "20260107105230846836",
                "OthersTaskTypeRunningInstanceCount": 0,
                "OthersTaskTypeSchedulingTaskCount": 0,
                "OthersTaskTypeWaitingInstanceCount": "0",
                "RunningInstanceCount": 3,
                "SchedulingTaskCount": 5,
                "WaitingInstanceCount": 3
            }
        ],
        "RequestId": "52a97d22-fea2-4cc3-86a8-5a1d8e5a4de0"
    }
}
```

