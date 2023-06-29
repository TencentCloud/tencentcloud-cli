**Example 1: 获取任务状态(增加任务流信息)**



Input: 

```
tccli acp DescribeScanTaskStatus --cli-unfold-argument  \
    --Platform 0 \
    --Source 2 \
    --TaskID 299***256 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6cf11eaf-e62d-40bd-ba61-4de8c7bfe14c",
        "Result": 0,
        "Status": 2,
        "FlowSteps": [
            {
                "FlowNo": "1.1",
                "FlowName": "APK 下载",
                "FlowStatus": 2,
                "FlowStateDesc": "成功",
                "StartTime": "2022-04-06 16:31:39",
                "EndTime": "2022-04-06 18:25:27"
            },
            {
                "FlowNo": "1.2",
                "FlowName": "APK 校验",
                "FlowStatus": 2,
                "FlowStateDesc": "成功",
                "StartTime": "2022-04-06 16:31:39",
                "EndTime": "2022-04-06 18:25:27"
            },
            {
                "FlowNo": "2.1",
                "FlowName": "隐私文本下载",
                "FlowStatus": 2,
                "FlowStateDesc": "成功",
                "StartTime": "2022-04-06 16:59:40",
                "EndTime": "2022-04-06 16:59:40"
            },
            {
                "FlowNo": "2.1.1",
                "FlowName": "隐私文本解析",
                "FlowStatus": 2,
                "FlowStateDesc": "成功",
                "StartTime": "2022-04-06 17:01:42",
                "EndTime": "2022-04-06 17:06:46"
            },
            {
                "FlowNo": "2.1",
                "FlowName": "自研引擎(APK)",
                "FlowStatus": 2,
                "FlowStateDesc": "成功",
                "StartTime": "2022-04-06 17:01:42",
                "EndTime": "2022-04-06 18:18:21"
            },
            {
                "FlowNo": "2.2",
                "FlowName": "自研引擎(APK+隐私文本)",
                "FlowStatus": 2,
                "FlowStateDesc": "成功",
                "StartTime": "2022-04-06 18:18:21",
                "EndTime": "2022-04-06 18:23:23"
            },
            {
                "FlowNo": "3.1",
                "FlowName": "隐私检测综合判定",
                "FlowStatus": 2,
                "FlowStateDesc": "成功",
                "StartTime": "2022-04-06 18:23:23",
                "EndTime": "2022-04-06 18:25:27"
            }
        ],
        "ErrMsg": "成功"
    }
}
```

