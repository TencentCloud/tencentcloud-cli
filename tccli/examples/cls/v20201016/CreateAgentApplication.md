**Example 1: 创建agent可观测应用**



Input: 

```
tccli cls CreateAgentApplication --cli-unfold-argument  \
    --ApplicationName ***********st_agent \
    --AccessType Langfuse \
    --LogsetId leotest-custom-logset-1254077820
```

Output: 
```
{
    "Response": {
        "ApplicationId": "agent-app-3ca04119-f707-49c9-9d93-b79114c18042",
        "LogTopics": [
            {
                "Flag": "trace",
                "TopicId": "d8886b56-eecc-45ea-8c7c-639348c764e8"
            }
        ],
        "MetricsTopics": [],
        "RequestId": "92de2157-5971-4d19-b561-9b2587067d0b"
    }
}
```

