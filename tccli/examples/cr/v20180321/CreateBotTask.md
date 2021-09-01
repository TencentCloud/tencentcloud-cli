**Example 1: 创建机器人任务**



Input: 

```
tccli cr CreateBotTask --cli-unfold-argument  \
    --Module AiApi \
    --Operation CreateTask \
    --BotName qtest01 \
    --FlowId abc123456000000 \
    --CallTimeCollection.Monday.EndTime 160000 \
    --CallTimeCollection.Monday.StartTime 080000 \
    --CallTimeCollection.Tuesday.EndTime 160000 \
    --CallTimeCollection.Tuesday.StartTime 080000 \
    --CallTimeCollection.Friday.EndTime 160000 \
    --CallTimeCollection.Friday.StartTime 080000 \
    --CallTimeCollection.Wednesday.EndTime 160000 \
    --CallTimeCollection.Wednesday.StartTime 080000 \
    --CallTimeCollection.Thursday.EndTime 160000 \
    --CallTimeCollection.Thursday.StartTime 080000 \
    --CallTimeCollection.Sunday.EndTime 160000 \
    --CallTimeCollection.Sunday.StartTime 080000 \
    --CallTimeCollection.Saturday.EndTime 160000 \
    --CallTimeCollection.Saturday.StartTime 080000 \
    --BanCall Y \
    --StartTimeBan 120000 \
    --EndTimeBan 130000 \
    --PhoneCollection 01ABC \
    --CallCount 1 \
    --CallInterval 5
```

Output: 
```
{
    "Response": {
        "RequestId": "12345-6789-test-from-rest4api",
        "BotId": "zc"
    }
}
```

