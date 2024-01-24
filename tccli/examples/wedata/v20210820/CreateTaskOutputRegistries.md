**Example 1: 批量添加产出登记项**

批量添加产出登记项

Input: 

```
tccli wedata CreateTaskOutputRegistries --cli-unfold-argument  \
    --Registries.0.TaskId abc \
    --Registries.0.TaskName abc \
    --Registries.0.ProjectId abc \
    --Registries.0.DatasourceId abc \
    --Registries.0.DatabaseName abc \
    --Registries.0.TableName abc \
    --Registries.0.TableGuid abc \
    --Registries.0.PartitionName abc \
    --Registries.0.DbGuid abc \
    --Registries.0.TablePhysicalId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "abc",
                "TaskName": "abc",
                "ProjectId": "abc",
                "DatasourceId": "abc",
                "DatabaseName": "abc",
                "TableName": "abc",
                "TableGuid": "abc",
                "PartitionName": "abc",
                "Id": 0,
                "AppId": "abc",
                "DataFlowType": "abc",
                "CreateTime": "abc",
                "UserUin": "abc",
                "OwnerUin": "abc",
                "Ext": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

