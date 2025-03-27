**Example 1: ExecuteCommandOnAndroidInstances 示例**



Input: 

```
tccli gs ExecuteCommandOnAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds cai-abcd1234 \
    --Command ls
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "615cf0a4-075e-4cf5-b26f-d786363dacce"
            }
        ],
        "RequestId": "requestid"
    }
}
```

