**Example 1: 查询资源推送任务列表**



Input: 

```
tccli iotcloud DescribeResourceTasks --cli-unfold-argument  \
    --ProductID ' EQPOKD5111' \
    --Name dev-001 \
    --Offset 1 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "Total": 53,
        "TaskInfos": [
            {
                "TaskId": 1000175,
                "Status": 3,
                "CreateTime": 1589466879,
                "Type": 1
            },
            {
                "TaskId": 1000176,
                "Status": 3,
                "CreateTime": 1589467049,
                "Type": 1
            },
            {
                "Status": 3,
                "CreateTime": 1589467138,
                "Type": 1,
                "TaskId": 1000179
            },
            {
                "TaskId": 1000180,
                "Status": 3,
                "CreateTime": 1589467139,
                "Type": 1
            },
            {
                "Type": 1,
                "TaskId": 1000182,
                "Status": 3,
                "CreateTime": 1589467141
            }
        ],
        "RequestId": "ebea2fd8-0b8f-44b3-99ab-1b04fcfb6cbd"
    }
}
```

