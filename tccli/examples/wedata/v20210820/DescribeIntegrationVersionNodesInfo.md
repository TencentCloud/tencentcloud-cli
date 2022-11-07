**Example 1: 查询集成任务版本节点信息**

查询集成任务版本节点信息

Input: 

```
tccli wedata DescribeIntegrationVersionNodesInfo --cli-unfold-argument  \
    --TaskId cos-|ap-|file.dg \
    --ProjectId 22yy \
    --TaskVersionPath cos-|ap-|file_xxy.dg \
    --TaskVersion xx
```

Output: 
```
{
    "Response": {
        "TaskId": "cos-|ap-|file.dg",
        "RequestId": "xx",
        "Nodes": [
            {
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
            }
        ],
        "Mappings": [
            {
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
            }
        ]
    }
}
```

