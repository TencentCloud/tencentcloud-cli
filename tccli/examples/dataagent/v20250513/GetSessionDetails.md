**Example 1: 获取会话详情**

获取会话详情

Input: 

```
tccli dataagent GetSessionDetails --cli-unfold-argument  \
    --InstanceId dataagent-hLhMpd0H \
    --SessionId ee8b5304-3ef0-4942-beb2-8c9354a3ed4e
```

Output: 
```
{
    "Response": {
        "RequestId": "631bb90d-ea0f-4dfe-abd5-515d34e67ef6",
        "RecordList": [
            {
                "Context": "{\"KnowledgeBases\":[{\"KnowledgeBaseId\":\"klbase-kSnxsssvrXI\",\"FileIds\":[],\"Databases\":[{\"MCP\":{\"Instance\":\"mcp-apssyb72s\",\"Type\":\"TCHouseD\",\"Url\":\"http://10.0.0.90:31234/sse?key=xxxxxx\",\"DataEngineName\":\"官方数据源\",\"IsSampling\":true,\"TCCatalogName\":\"官方数据源\",\"DataSourceId\":\"datasource_tchoused_example\",\"DataSourceInstanceId\":\"cdwdoris-62xxxxlnh\"}}]}]}",
                "Question": "who are you",
                "Answer": "Hello! I'm your data analysis assistant here to help with your data-related queries and tasks.",
                "Think": "Analyzing your request... Detected small talk based on your input.",
                "TaskList": [],
                "FinalSummary": "{\"v\": \"\", \"cell_id\": \"\"}",
                "CreateTime": "2025-11-14T02:45:43.369206+00:00",
                "UpdateTime": "2025-11-14T02:45:43.369210+00:00",
                "RecordId": "63eb66d2-a80a-4d57-9a80-68befed2f388",
                "Feedback": 0,
                "SessionId": "ee8b5304-3ef0-4942-beb2-8c9354a3ed4e",
                "DbInfo": "",
                "ErrorContext": "",
                "TaskListStr": "",
                "KnowledgeBaseIds": [
                    "klbase-kSnxNtvrXI"
                ]
            },
            {
                "Context": "{\"KnowledgeBases\":[{\"KnowledgeBaseId\":\"klbase-kSnxsssvrXI\",\"FileIds\":[],\"Databases\":[{\"MCP\":{\"Instance\":\"mcp-apssyb72s\",\"Type\":\"TCHouseD\",\"Url\":\"http://10.0.0.90:31234/sse?key=xxxxxx\",\"DataEngineName\":\"官方数据源\",\"IsSampling\":true,\"TCCatalogName\":\"官方数据源\",\"DataSourceId\":\"datasource_tchoused_example\",\"DataSourceInstanceId\":\"cdwdoris-62xxxxlnh\"}}]}]}",
                "Question": "what are you doing?",
                "Answer": "I'm here and ready to assist you with any data analysis or related tasks you might have!",
                "Think": "Analyzing your request... Detected small talk based on your input.",
                "TaskList": [],
                "FinalSummary": "{\"v\": \"\", \"cell_id\": \"\"}",
                "CreateTime": "2025-11-14T02:46:51.806983+00:00",
                "UpdateTime": "2025-11-14T02:46:51.806985+00:00",
                "RecordId": "5b13dd3b-96cf-4d4d-a6f0-13555a1f9fb8",
                "Feedback": 0,
                "SessionId": "ee8b5304-3ef0-4942-beb2-8c9354a3ed4e",
                "DbInfo": "",
                "ErrorContext": "",
                "TaskListStr": "",
                "KnowledgeBaseIds": [
                    "klbase-kSnxNtvrXI"
                ]
            }
        ],
        "RecordCount": 2,
        "RunRecord": ""
    }
}
```

