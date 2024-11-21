**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli vclm DescribeVideoTranslateJob --cli-unfold-argument  \
    --JobId vlSYvQkMM0KwPuoakawm0tPrREwc2p7c
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.JobNotExist",
            "Message": "任务不存在。"
        },
        "RequestId": "78254ad1-c184-4e9e-b5a0-9d3fc435576b"
    }
}
```

**Example 2: 调用成功示例**

调用成功示例

Input: 

```
tccli vclm DescribeVideoTranslateJob --cli-unfold-argument  \
    --JobId vlSYvQkMM0KwPuoakawm0tPrREwc2p7c
```

Output: 
```
{
    "Response": {
        "AsrTimestamps": [
            {
                "EndMs": 14080,
                "StartMs": 360,
                "Text": "当工作或学习结果不理想，甚至面临被全盘否定的情况时，你会如何应对？可以举例说明当时你是如何处理负面情绪，并找到解决办法的。"
            }
        ],
        "JobAudioModerationId": "",
        "JobAudioTaskId": "b409e6d8f22849cfa472b162370c6ed0",
        "JobConfirm": 0,
        "JobErrorCode": "FailedOperation.Success",
        "JobErrorMsg": "成功。",
        "JobStatus": 8,
        "JobSubmitReqId": "7cdf871b-cbb3-4493-87ba-dbaff29b1012",
        "JobVideoId": "1248894010240876544",
        "JobVideoModerationId": "1248893756036694016",
        "RequestId": "a974b772-3c1d-4868-8909-b1386016b9f0",
        "OriginalVideoUrl": "http://console.cloud.tencent.com/cos/video.mp4",
        "ResultVideoUrl": "https://tencent.cos.ap-guangzhou.myqcloud.com/video_translate/output/video.mp4",
        "TranslateResults": [
            {
                "SourceText": "当工作或学习结果不理想，甚至面临被全盘否定的情况时，你会如何应对？可以举例说明当时你是如何处理负面情绪，并找到解决办法的。",
                "TargetText": "How do you cope when work or academic results are not ideal, or even when faced with a complete denial of your efforts? Provide an example of how you managed negative emotions and found a solution in such a situation."
            }
        ]
    }
}
```

