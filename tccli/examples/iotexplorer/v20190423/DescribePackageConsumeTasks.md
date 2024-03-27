**Example 1: 查询套餐消耗记录列表**



Input: 

```
tccli iotexplorer DescribePackageConsumeTasks --cli-unfold-argument  \
    --Limit 45 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a9545416-7eac-4e2e-a4a0-9735b0ee7682",
        "TotalCount": 3,
        "List": [
            {
                "TaskId": 3,
                "CreateTime": "2022-02-18 15:45:06",
                "State": 3
            },
            {
                "TaskId": 2,
                "CreateTime": "2022-02-18 15:43:38",
                "State": 3
            },
            {
                "TaskId": 1,
                "CreateTime": "2022-02-17 14:50:42",
                "State": 3
            }
        ]
    }
}
```

