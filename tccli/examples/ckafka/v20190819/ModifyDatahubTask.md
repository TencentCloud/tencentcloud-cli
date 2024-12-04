**Example 1: 修改Datahub任务**



Input: 

```
tccli ckafka ModifyDatahubTask --cli-unfold-argument  \
    --TaskId task-test \
    --TaskName taskname
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-tes"
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0"
    }
}
```

