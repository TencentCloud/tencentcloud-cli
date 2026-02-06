**Example 1: 暂停Datahub任务**



Input: 

```
tccli ckafka PauseDatahubTask --cli-unfold-argument  \
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

