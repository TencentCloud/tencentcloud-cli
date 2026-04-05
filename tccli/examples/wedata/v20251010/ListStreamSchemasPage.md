**Example 1: 示例1**

示例1

Input: 

```
tccli wedata ListStreamSchemasPage --cli-unfold-argument  \
    --MaxResults 1000 \
    --PageToken 0 \
    --DatabaseName dbA \
    --ConnectionId 123123213 \
    --ConnectionType Oracle \
    --WorkspaceId 312312312 \
    --Keyword 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "SchemaName": "mock_schema_1"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "2e63b834-cb0e-417b-a693-f21eac5da845"
    }
}
```

