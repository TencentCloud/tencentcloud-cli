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

**Example 2: 示例2**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "81a92494-0fb9-4b10-8ce4-bfa4565cf4eb",
        "TaskSet": null,
        "Total": 0
    }
}
```

**Example 3: 示例3**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "11483de9-9be5-4537-a846-339a57f0e90e",
        "TaskSet": null,
        "Total": 0
    }
}
```

**Example 4: 示例5**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "d7628289-fd3c-4acf-a140-a33dd02b3ff6",
        "TaskSet": null,
        "Total": 0
    }
}
```

