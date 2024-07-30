**Example 1: 获取查询任务列表**

获取查询任务列表

Input: 

```
tccli dnshg DescribeQueryTask --cli-unfold-argument  \
    --Filters.0.Name TaskId \
    --Filters.0.Values gggg
```

Output: 
```
{
    "Response": {
        "RequestId": "493f3e26-55f5-46ee-bc21-3e46cd4d59ec",
        "TaskList": [
            {
                "Contents": [
                    "s.fs2.dfsdf2"
                ],
                "CreatedAt": "2024-05-24 11:34:10",
                "EndTime": "2024-05-18",
                "Result": "https://pdns-release-fz-prelog-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/hg_log_result/tid-YF1GkvEhBA/result.txt?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEPrPr6DLMLMKBxmXTfp7NbryF3qfZTTb%26q-sign-time%3D1716542882%3B1717147682%26q-key-time%3D1716542882%3B1717147682%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D4d79d6cc735134659be0ab1915be3af5670c06fb",
                "StartTime": "2024-05-18",
                "Status": 1,
                "TaskId": "tid-YF1GkvEhBA",
                "TaskType": 2
            }
        ],
        "TotalCount": 1
    }
}
```

