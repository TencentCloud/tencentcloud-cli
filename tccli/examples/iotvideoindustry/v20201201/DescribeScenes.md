**Example 1: 获取场景列表**



Input: 

```
tccli iotvideoindustry DescribeScenes --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "IntId": 1,
                "Uin": "2",
                "SceneName": "测试场景",
                "SceneTrigger": "{22222}",
                "RecordDuration": 360,
                "StoreDuration": 2,
                "CreateTime": "2021-10-21T19:22:58+08:00",
                "UpdateTime": "2021-10-21T19:22:58+08:00"
            },
            {
                "IntId": 2,
                "Uin": "2",
                "SceneName": "测试场景1",
                "SceneTrigger": "{2222211}",
                "RecordDuration": 3600,
                "StoreDuration": 2,
                "CreateTime": "2021-10-21T19:34:21+08:00",
                "UpdateTime": "2021-10-21T19:40:14+08:00"
            }
        ],
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f",
        "Total": 2
    }
}
```

