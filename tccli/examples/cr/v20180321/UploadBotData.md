**Example 1: 上传机器人任务数据**



Input: 

```
tccli cr UploadBotData --cli-unfold-argument  \
    --Module AiApi \
    --Operation UploadData \
    --Data  \
    --BotId xx \
    --BotName qtest01
```

Output: 
```
{
    "Response": {
        "RequestId": "12345-6789-test-from-rest4api"
    }
}
```

