**Example 1: 告警级别列表**

成功响应

Input: 

```
tccli weilingwith DescribeAlarmLevelList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "54b9f3e5-9e78-43aa-92b6-d895d31372d6",
        "Result": {
            "AlarmLevelSet": [
                {
                    "LevelId": 3,
                    "LevelName": "严重"
                },
                {
                    "LevelId": 4,
                    "LevelName": "紧急"
                },
                {
                    "LevelId": 5,
                    "LevelName": "致命"
                },
                {
                    "LevelId": 1,
                    "LevelName": "提示"
                },
                {
                    "LevelId": 2,
                    "LevelName": "一般"
                }
            ]
        }
    }
}
```

