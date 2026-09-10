**Example 1: 查询MCP Tools导入任务的进度**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayMCPToolImportTask --cli-unfold-argument  \
    --GatewayId gateway-6fa655a5 \
    --MCPServerId 2dd8373d-16e9-4f43-9808-5aa75fcfc097
```

Output: 
```
{
    "Response": {
        "Result": {
            "FailedCount": 0,
            "ProcessedCount": 1,
            "SuccessCount": 1,
            "TaskEndTime": "2026-04-15 16:19:26",
            "TaskId": "task-c93d9ca5",
            "TaskStartTime": "2026-04-15 16:19:22",
            "TaskStatus": "End",
            "ToolsImportResult": [
                {
                    "FailedMessage": null,
                    "Method": "POST",
                    "Name": "createPet-3",
                    "Path": "/anything",
                    "Status": "Success",
                    "UpstreamUrl": ""
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "941cb4db-6f8c-4f36-b4ac-19d3476cd7b6"
    }
}
```

