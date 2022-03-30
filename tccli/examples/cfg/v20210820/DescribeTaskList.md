**Example 1: 查询演练列表**



Input: 

```
tccli cfg DescribeTaskList --cli-unfold-argument  \
    --Limit 10 \
    --TaskTag 飞扬 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "47e12dca-fa37-49b4-86e1-d7d3d7674640",
        "TaskList": [
            {
                "TaskId": 2,
                "TaskTitle": "广州二区-关机",
                "TaskDescription": "广州一区-关机",
                "TaskTag": "飞扬",
                "TaskStatus": 1002,
                "TaskCreateTime": "2021-08-14 00:37:34",
                "TaskUpdateTime": "2021-09-18 19:18:28"
            }
        ],
        "Total": 1
    }
}
```

