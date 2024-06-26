**Example 1: 修改Datahub任务**



Input: 

```
tccli ckafka ModifyDatahubTask --cli-unfold-argument  \
    --TaskId abc \
    --TaskName abc
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

