**Example 1: 发起生成 AIGC 视频的任务**



Input: 

```
tccli vod CreateAigcVideoTask --cli-unfold-argument  \
    --SubAppId 251007502 \
    --ModelName GV \
    --ModelVersion 3.1-fast \
    --FileInfos.0.FileId 3704211***509819 \
    --LastFrameFileId 3704211***509911 \
    --Prompt generate a car \
    --NegativePrompt red \
    --EnhancePrompt Enabled \
    --OutputConfig.StorageMode Temporary \
    --OutputConfig.AspectRatio 9:16 \
    --OutputConfig.AudioGeneration Enabled \
    --OutputConfig.PersonGeneration AllowAdult \
    --OutputConfig.InputComplianceCheck Enabled \
    --OutputConfig.OutputComplianceCheck Enabled \
    --SessionId mysession2 \
    --SessionContext mysessionContext \
    --TasksPriority 10 \
    --ExtInfo myextinfo
```

Output: 
```
{
    "Response": {
        "TaskId": "251007502-AigcVideo***25dacdcef7dd2b20fdt",
        "RequestId": "d68920a4-c989-4afe-ac4d-2f06de99368e"
    }
}
```

