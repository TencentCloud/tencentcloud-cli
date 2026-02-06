**Example 1: 恢复Datahub任务**



Input: 

```
tccli ckafka ResumeDatahubTask --cli-unfold-argument  \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "abc"
        },
        "RequestId": "abc"
    }
}
```

