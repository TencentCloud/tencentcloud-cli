**Example 1: 按类型查询拨测任务列表 示例**



Input: 

```
tccli cat DescribeTasksByType --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Tasks": [
            {
                "TaskId": 210837,
                "TaskName": "HelpToTestBaidu",
                "Period": 5,
                "CatTypeName": "http",
                "Status": 1,
                "CgiUrl": "http://www.baidu.com",
                "AddTime": "2019-12-11 19:28:58",
                "UpdateTime": "2019-12-11 20:01:08",
                "AlarmStatus": 0,
                "StatusInfo": "全部节点拨测正常"
            }
        ],
        "RequestId": "8f6bf02b-4699-45fe-b664-1f9813efff76"
    }
}
```

