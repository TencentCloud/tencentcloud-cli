**Example 1: 任务成功完成**

任务成功完成，返回结果视频Url

Input: 

```
tccli vclm DescribeTemplateToVideoJob --cli-unfold-argument  \
    --JobId 1305546906952867840
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "RequestId": "17288c38-8b83-4ad2-a818-ef2d2d87dfe7",
        "ResultVideoUrl": "https://console.cloud.tencent.com/result.mp4",
        "Status": "DONE"
    }
}
```

