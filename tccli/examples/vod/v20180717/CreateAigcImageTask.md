**Example 1: 发起生成 AIGC 图片的任务**



Input: 

```
tccli vod CreateAigcImageTask --cli-unfold-argument  \
    --SubAppId 251007502 \
    --ModelName GEM \
    --ModelVersion 2.5 \
    --FileInfos.0.FileId 3704211***509819 \
    --Prompt generate a car \
    --NegativePrompt red \
    --EnhancePrompt Enabled \
    --OutputConfig.StorageMode Temporary \
    --OutputConfig.AspectRatio 16:9 \
    --OutputConfig.PersonGeneration AllowAdult \
    --OutputConfig.InputComplianceCheck Enabled \
    --OutputConfig.OutputComplianceCheck Enabled \
    --SessionId mysession \
    --SessionContext mySessionContext \
    --TasksPriority 10 \
    --ExtInfo myextinfo
```

Output: 
```
{
    "Response": {
        "TaskId": "251007502-AigcImage***2782aff1e896673f1ft",
        "RequestId": "f50d7667-72d8-46bb-a7e3-0613588971b6"
    }
}
```

