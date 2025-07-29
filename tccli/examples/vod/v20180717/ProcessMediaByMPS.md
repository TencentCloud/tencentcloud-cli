**Example 1: 发起智能擦除任务**

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
        "TaskId": "125xxx65-ProcessMediaByMPS-bffb15f07530b57bc1aab01fac74bca"
    }
}
```

