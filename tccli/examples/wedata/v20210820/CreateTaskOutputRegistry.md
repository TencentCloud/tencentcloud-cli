**Example 1: 新增或编辑产出登记项**

新增或编辑产出登记项

Input: 

```
tccli wedata CreateTaskOutputRegistry --cli-unfold-argument  \
    --Id 0 \
    --TaskId abc \
    --TaskName abc \
    --ProjectId abc \
    --DatasourceId abc \
    --DatabaseName abc \
    --TableName abc \
    --TableGuid abc \
    --PartitionName abc \
    --DbGuid abc \
    --TablePhysicalId abc
```

Output: 
```
{
    "Response": {
        "Data": {
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
        },
        "RequestId": "abc"
    }
}
```

