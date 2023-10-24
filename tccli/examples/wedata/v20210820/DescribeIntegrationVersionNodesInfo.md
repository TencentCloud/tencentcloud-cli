**Example 1: 查询集成任务版本节点信息**

查询集成任务版本节点信息

Input: 

```
tccli wedata DescribeIntegrationVersionNodesInfo --cli-unfold-argument  \
    --TaskId ap-|cos-|file.dg \
    --ProjectId 123 \
    --TaskVersionPath YXAtfGNvcy18ZmlsZV94eC5kZw== \
    --TaskVersion 202310060503283
```

Output: 
```
{
    "Response": {
        "Nodes": [
            {
                "Id": "abc",
                "TaskId": "abc",
                "Name": "abc",
                "NodeType": "abc",
                "DataSourceType": "abc",
                "Description": "abc",
                "DatasourceId": "abc",
                "Config": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "ExtConfig": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "Schema": [
                    {
                        "Id": "abc",
                        "Name": "abc",
                        "Value": "abc",
                        "Type": "abc",
                        "Properties": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "Alias": "abc",
                        "Comment": "abc"
                    }
                ],
                "NodeMapping": {
                    "SourceId": "abc",
                    "SinkId": "abc",
                    "SourceSchema": [
                        {
                            "Id": "abc",
                            "Name": "abc",
                            "Value": "abc",
                            "Type": "abc",
                            "Alias": "abc",
                            "Comment": "abc",
                            "Properties": [
                                {
                                    "Name": "__key__",
                                    "Value": "abc"
                                }
                            ]
                        }
                    ],
                    "SchemaMappings": [
                        {
                            "SourceSchemaId": "abc",
                            "SinkSchemaId": "abc"
                        }
                    ]
                },
                "AppId": "abc",
                "ProjectId": "abc",
                "CreatorUin": "abc",
                "OperatorUin": "abc",
                "OwnerUin": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "Mappings": [
            {
                "SourceId": "abc",
                "SinkId": "abc",
                "SourceSchema": [
                    {
                        "Id": "abc",
                        "Name": "abc",
                        "Value": "abc",
                        "Type": "abc",
                        "Alias": "abc",
                        "Comment": "abc",
                        "Properties": []
                    }
                ],
                "SchemaMappings": [
                    {
                        "SourceSchemaId": "abc",
                        "SinkSchemaId": "abc"
                    }
                ]
            }
        ],
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

