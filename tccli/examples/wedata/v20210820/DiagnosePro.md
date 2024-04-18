**Example 1: 实例诊断**

实例运维-实例诊断

Input: 

```
tccli wedata DiagnosePro --cli-unfold-argument  \
    --ProjectId 155477816884 \
    --SearchCondition.Instance.TaskId 20240228175802766 \
    --SearchCondition.Instance.CurRunDate 2024-04-11 05:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": {
                "Diagnose": "任务并发判断不通过，实例：20240228175802766_2024-04-11 11:35:00",
                "Operation": "一般不用处理，等待平台自行调度处理。",
                "Reason": "当任务自依赖属性设置为无序串行时，任务实例只是无序的一个个处理，其他实例会排队等待",
                "TaskId": "20240228175802766",
                "TaskName": "geehivesql",
                "Url": ""
            },
            "Table": {
                "Column": [],
                "Data": []
            }
        },
        "RequestId": "c7083b20-a691-4aa3-bb5c-d2a6ef2bd45e"
    }
}
```

**Example 2: 实例诊断示例**

实例诊断

Input: 

```
tccli wedata DiagnosePro --cli-unfold-argument  \
    --SearchCondition.Instance.TaskId 20240307211852581 \
    --SearchCondition.Instance.CurRunDate 2024-04-10 00:00:00 \
    --ProjectId 1492511691706699776
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": {
                "Diagnose": "该实例执行失败",
                "Operation": "结合运行日志排查失败原因",
                "Reason": "用户代码和执行环境存在异常",
                "TaskId": "20240307211852581",
                "TaskName": "python_task_failed",
                "Url": ""
            },
            "Table": {
                "Column": [],
                "Data": []
            }
        },
        "RequestId": "cf111dff-a9c3-407d-83b5-d9424da7af12"
    }
}
```

