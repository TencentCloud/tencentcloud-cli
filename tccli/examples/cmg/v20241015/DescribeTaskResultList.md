**Example 1: 查询任务执行结果列表**

查询任务执行结果列表

Input: 

```
tccli cmg DescribeTaskResultList --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5tJbJqBV42pqoQafBDCd",
        "TotalCount": 10,
        "Items": [
            {
                "TaskID": "task-oQdm6gJ9",
                "TaskStatus": "task_success_cmg",
                "Progress": "",
                "StepList": [
                    {
                        "StepId": "prepare_param",
                        "StepName": "",
                        "Code": 200,
                        "Msg": "",
                        "Process": 0,
                        "Weight": 1
                    },
                    {
                        "StepId": "run_docker",
                        "StepName": "",
                        "Code": 200,
                        "Msg": "",
                        "Process": 0,
                        "Weight": 2
                    }
                ],
                "StartTime": "",
                "EndTime": ""
            }
        ]
    }
}
```

