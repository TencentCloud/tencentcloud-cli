**Example 1: 查询探测任务列表**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument  \
    --TaskIDs task-xx
```

Output: 
```
{
    "Response": {
        "Total": 3,
        "RequestId": "xx",
        "TaskSet": [
            {
                "Status": 1,
                "Name": "xx",
                "Parameters": "{}",
                "Interval": 30,
                "TaskId": "task-xx",
                "TaskType": 1,
                "Nodes": [
                    "10001"
                ]
            }
        ]
    }
}
```

