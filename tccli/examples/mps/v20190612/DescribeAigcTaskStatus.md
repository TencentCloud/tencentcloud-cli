**Example 1: 获取AIGC场景任务详情**



Input: 

```
tccli mps DescribeAigcTaskStatus --cli-unfold-argument  \
    --TaskId c50f6094-3b56-a1fa-e616-0eec386bfc36
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-06-01 20:40:50",
        "FinishedTime": "2026-06-01 20:44:32",
        "OutputUrl": "https://aigc-redraw-output-1326893053.cos.ap-guangzhou.myqcloud.com/aigc-c50f6094-3b56-a1fa-e616-0eec386bfc36-202606012044-0.mp4",
        "RequestBody": "{\"Input\":{\"Script\":\"从前有一只小兔子，上山采蘑菇\",\"Style\":\"chinese_ink_wash\",\"Ratio\":\"16:9\",\"Resolution\":\"720p\"},\"Action\":\"CreateAiDramaTask\",\"RequestId\":\"afbd7d37-888c-4cf5-959f-959a10ff4af6\",\"RequestSource\":\"API\",\"Uin\":\"600000563781\",\"ApiModule\":\"mps\",\"Timestamp\":\"1780317650\",\"ClientIp\":\"30.174.178.116\",\"SubAccountUin\":\"600000563781\",\"Region\":\"\",\"RequestClient\":\"APIExplorer\",\"AppId\":1300057355}",
        "ScheduledTime": "2026-06-01 20:40:51",
        "TaskId": "c50f6094-3b56-a1fa-e616-0eec386bfc36",
        "TaskStatus": "FINISHED",
        "TaskType": "AIDrama",
        "RequestId": "9ee02d10-a534-4a2d-842a-c4d084bcfbde"
    }
}
```

