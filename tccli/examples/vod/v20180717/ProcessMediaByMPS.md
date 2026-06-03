**Example 1: 使用MPSProcessMediaParams参数发起智能分析任务**

使用MPSProcessMediaParams参数发起智能分析任务

Input: 

```
tccli vod ProcessMediaByMPS --cli-unfold-argument  \
    --FileId 966263619095884274 \
    --SubAppId 221157 \
    --MPSProcessMediaParams {"AiAnalysisTask":{"Definition": 21,"ExtendedParameter":""}}
```

Output: 
```
{
    "Response": {
        "TaskId": "221157-ProcessMediaByMPS-c80d6b074ba566e4e4097bccc0044b9bt",
        "RequestId": "4cc2a86b-7463-4ac2-9a32-e64882716f9e"
    }
}
```

**Example 2: 使用结构化参数发起智能分析任务**

使用结构化参数发起智能分析任务

Input: 

```
tccli vod ProcessMediaByMPS --cli-unfold-argument  \
    --FileId 966263619095884274 \
    --SubAppId 221157 \
    --AiAnalysisTask.Definition 21 \
    --AiAnalysisTask.ExtendedParameter 
```

Output: 
```
{
    "Response": {
        "TaskId": "221157-ProcessMediaByMPS-fd5bcd2cf2195fda7c7b571aa18cb68dt",
        "RequestId": "c8bbd537-0815-4123-b284-8c1ee856bbe8"
    }
}
```

