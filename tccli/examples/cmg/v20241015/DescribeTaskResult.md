**Example 1: 查询任务执行结果**

查询任务执行结果

Input: 

```
tccli cmg DescribeTaskResult --cli-unfold-argument  \
    --TaskID task-ZQqiMPrE
```

Output: 
```
{
    "Response": {
        "Data": {
            "EndTime": "",
            "Progress": "",
            "StartTime": "",
            "StepList": [
                {
                    "Code": 200,
                    "Msg": "",
                    "Process": 0,
                    "StepId": "prepare_param",
                    "StepName": "",
                    "Weight": 1
                },
                {
                    "Code": 200,
                    "Msg": "",
                    "Process": 0,
                    "StepId": "run_docker",
                    "StepName": "",
                    "Weight": 2
                }
            ],
            "TaskID": "task-ZQqiMPrE",
            "TaskStatus": "task_success_cmg"
        },
        "RequestId": "3cff65c3-4d99-417d-a90f-90a26cb0a97e"
    }
}
```

