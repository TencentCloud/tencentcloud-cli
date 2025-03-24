**Example 1: ExecuteCommandOnAndroidInstances 示例**



Input: 

```
tccli gs ExecuteCommandOnAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds abc \
    --Command abc
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "abc"
            }
        ],
        "RequestId": "requestid"
    }
}
```

