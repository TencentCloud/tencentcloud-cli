**Example 1: 查询agent可观测应用列表**



Input: 

```
tccli cls DescribeAgentApplications --cli-unfold-argument  \
    --Filters.0.Key accessType \
    --Filters.0.Values Langfuse \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "AccessType": "Langfuse",
                "ApplicationId": "agent-app-3ca04119-f707-49c9-9d93-b79114c18042",
                "ApplicationName": "update_agent_application",
                "CreateTime": 1782740118,
                "LogTopics": [
                    {
                        "Flag": "trace",
                        "TopicId": "d8886b56-eecc-45ea-8c7c-639348c764e8"
                    }
                ],
                "MetricsTopics": [],
                "Region": "ap-gu************",
                "UpdateTime": 1783309827
            }
        ],
        "Total": 3,
        "RequestId": "ee40acd4-1663-4364-935f-07fe726c6eef"
    }
}
```

