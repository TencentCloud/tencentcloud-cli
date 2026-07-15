**Example 1: 上传文件并创建 TWeSee 语义理解任务**



Input: 

```
tccli iotexplorer CreateTWeSeeRecognitionTaskWithFile --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ChannelId 0 \
    --CustomId event-1 \
    --EnableSearch True \
    --StartTimeMs 1761201772000 \
    --EndTimeMs 1761201779000 \
    --Config config_content \
    --IsCustomDevice False \
    --InputType video \
    --SummaryQOS minutely \
    --ServiceType Summary \
    --InputBase64 AAAAIGZ0eXBpc29tAAAC...
```

Output: 
```
{
    "Response": {
        "TaskId": "019a0fdd-81ed-7f89-911a-43e2a0df1c2d",
        "RequestId": "665a49ba-120b-4447-9a43-4f303d47b886"
    }
}
```

