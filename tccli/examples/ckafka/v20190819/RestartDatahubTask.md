**Example 1: 重启Datahub任务**



Input: 

```
tccli ckafka RestartDatahubTask --cli-unfold-argument  \
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

