**Example 1: 查询演练列表**

查询演练列表

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
                "TaskUpdateTime": "2021-09-18 19:18:28",
                "TaskPreCheckStatus": 0,
                "TaskPreCheckSuccess": false
            }
        ],
        "Total": 1
    }
}
```

**Example 2: 查询演练列表(含预检状态信息)**

查询演练列表(含预检状态信息)

Input: 

```
tccli cfg DescribeTaskList --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "597dbef8-fcf3-46c2-9561-f87694052606",
        "TaskList": [
            {
                "TaskId": 3077,
                "TaskTitle": "演练预检测试",
                "TaskDescription": "演练预检测试",
                "TaskTag": "",
                "TaskStatus": 1001,
                "TaskCreateTime": "2022-09-19 12:57:22",
                "TaskUpdateTime": "2022-09-19 12:57:22",
                "TaskPreCheckStatus": 2,
                "TaskPreCheckSuccess": false
            },
            {
                "TaskId": 3076,
                "TaskTitle": "【公有云】Mongo节点故障",
                "TaskDescription": "【公有云】Mongo节点故障",
                "TaskTag": "",
                "TaskStatus": 1003,
                "TaskCreateTime": "2022-09-19 11:09:50",
                "TaskUpdateTime": "2022-09-19 12:17:49",
                "TaskPreCheckStatus": 0,
                "TaskPreCheckSuccess": false
            }
        ],
        "Total": 2450
    }
}
```

