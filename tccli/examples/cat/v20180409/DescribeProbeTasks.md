**Example 1: 查询拨测任务列表**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument  \
    --TaskIDs task-xx \
    --TagFilters.0.Key name \
    --TagFilters.0.Value zhangsan
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
                ],
                "TagInfoList": [
                    {
                        "Key": "tag_key1",
                        "Value": "tag_value1"
                    }
                ]
            }
        ]
    }
}
```

