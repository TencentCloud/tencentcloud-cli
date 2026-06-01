**Example 1: QuerySparkTaskLog**

查询spark 任务日志

Input: 

```
tccli tchousex QuerySparkTaskLog --cli-unfold-argument  \
    --TaskId batch-task-12334 \
    --PodName batch-task-12334-driver \
    --StartTime 0 \
    --EndTime 0 \
    --Context  \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "Context": "Y29udGV4dC1lNGM0YjlkMy1kNTcyLTRjZDItOTg0Ni1hMDk3YmJjMjMyNTAxNzI0MTQyODg1NjQ3",
        "SparkLogList": [
            "[INFO]java.xxx"
        ],
        "RequestId": "d78d6164-fe63-4b1d-956a-d148841ff424"
    }
}
```

