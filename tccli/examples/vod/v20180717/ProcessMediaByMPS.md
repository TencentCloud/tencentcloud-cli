**Example 1: 发起智能分析高光任务**

对 fileId 为 5285485487985271487 的视频发起智能分析高光任务。

Input: 

```
tccli vod ProcessMediaByMPS --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --SubAppId 1500000001 \
    --MPSProcessMediaParams {"AiAnalysisTask":{"Definition": 26,"ExtendedParameter":""}}
```

Output: 
```
{
    "Response": {
        "TaskId": "1500000001-ProcessMediaByMPS-29700e29ad5d252175d009042e09f30ft",
        "RequestId": "7987d7bd-068e-4138-863e-b63208bd0f6b"
    }
}
```

**Example 2: 发起智能擦除任务**

对 fileId 为 5285485487985271487 的视频发起智能擦除任务。

Input: 

```
tccli vod ProcessMediaByMPS --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --SubAppId 1500000001 \
    --MPSProcessMediaParams {"AiAnalysisTask": {"Definition":25,"ExtendedParameter":"{\"delogo\":{\"cluster_id\":\"gpu_zhiyan\",\"CustomerAppId\":\"subtitle_erase_fast\"}}"}}
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "1500000001-ProcessMediaByMPS-bffb15f07530b57bc1aab01fac74bca"
    }
}
```

**Example 3: 发起自定义模版转码任务**

对 fileId 为 5285485487985271487 的视频发起自定义模版转码任务。

Input: 

```
tccli vod ProcessMediaByMPS --cli-unfold-argument  \
    --FileId 5285485487985271487 \
    --SubAppId 1500000001 \
    --MPSProcessMediaParams {"MediaProcessTask":{"TranscodeTaskSet":[{"Definition":10101001}]}}
```

Output: 
```
{
    "Response": {
        "TaskId": "1500000001-ProcessMediaByMPS-c356d99d90c78c9fc7fac06641edf0d7t",
        "RequestId": "499738f8-bc4d-4e52-ab6e-9b7552c25a0f"
    }
}
```

