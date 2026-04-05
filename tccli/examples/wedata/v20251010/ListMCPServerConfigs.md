**Example 1: ListMCPServerConfigs**



Input: 

```
tccli wedata ListMCPServerConfigs --cli-unfold-argument  \
    --WorkspaceId 17726165045208090
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreatedBy": "700002164619",
                    "CreatedOn": "1774424096347",
                    "CreatedUser": "wedata30-test1@tencent.com",
                    "Description": "tavilyMCP工具描述",
                    "Key": "f07b2efa1774424096340dd159739",
                    "ModifiedBy": "700002164619",
                    "ModifiedOn": "1774424096347",
                    "ModifiedUser": "wedata30-test1@tencent.com",
                    "ServerName": "tavily",
                    "ServerType": "external",
                    "ServerUrl": "https://mcp.wedataapp-dev.cloud.tencent.com/api/1.0/mcp/http/external/f07b2efa1774424096340dd159739",
                    "Status": "active",
                    "TransportType": "streamable-http",
                    "WorkspaceId": "17726165045208090"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 2,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "3d47962a-266e-487f-98d3-1dc5d16098c7"
    }
}
```

