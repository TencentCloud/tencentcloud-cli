**Example 1: DescribeIntegrationNode**

查询集成节点

Input: 

```
tccli wedata DescribeIntegrationNode --cli-unfold-argument  \
    --ProjectId xx \
    --Id xx \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "NodeInfo": {
            "NodeType": "xx",
            "Description": "xx",
            "CreatorUin": "xx",
            "DataSourceType": "xx",
            "ProjectId": "xx",
            "OwnerUin": "xx",
            "ExtConfig": [
                {
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "DatasourceId": "xx",
            "NodeMapping": {
                "SourceId": "xx",
                "SchemaMappings": [
                    {
                        "SinkSchemaId": "xx",
                        "SourceSchemaId": "xx"
                    }
                ],
                "SinkId": "xx",
                "SourceSchema": [
                    {
                        "Type": "xx",
                        "Id": "xx",
                        "Value": "xx",
                        "Name": "xx"
                    }
                ]
            },
            "TaskId": "xx",
            "AppId": "xx",
            "Schema": [
                {
                    "Type": "xx",
                    "Id": "xx",
                    "Value": "xx",
                    "Name": "xx"
                }
            ],
            "Config": [
                {
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "Id": "xx",
            "OperatorUin": "xx",
            "Name": "xx"
        },
        "SourceCheckFlag": false,
        "RequestId": "xx"
    }
}
```

