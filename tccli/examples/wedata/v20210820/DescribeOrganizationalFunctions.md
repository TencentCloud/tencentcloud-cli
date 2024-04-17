**Example 1: 查询全量函数（层级化）接口**



Input: 

```
tccli wedata DescribeOrganizationalFunctions --cli-unfold-argument  \
    --ProjectId 1531609696090365952 \
    --Type FUNC_DEVELOP \
    --Name test \
    --DisplayName test
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Category": "CUSTOM",
                "Status": "EFFECTIVE",
                "Kind": "ANALYSIS",
                "DisplayName": "Hive SQL 函数",
                "Name": "hive_01",
                "OwnerUserIds": [
                    0
                ],
                "ReturnDesc": "test",
                "FuncId": "d65df5af-28b4-4171-9a24-ce96fc4e83fa",
                "ParamDesc": "test",
                "Example": "",
                "ClassName": "demoClass",
                "ResourceList": [
                    {
                        "Comment": "test",
                        "UserName": "test",
                        "Timestamp": "20240101",
                        "UserId": "4563234",
                        "Content": "test",
                        "Tag": "tag",
                        "Type": "HIVE"
                    }
                ],
                "OperatorUserIds": [
                    0
                ],
                "Usage": "UDFRepeat(var,2)",
                "ClusterIdentifier": "fpgreitj",
                "LayerPath": "/HIVE/CUSTOM",
                "Type": "HIVE",
                "SubmitErrorMsg": "test",
                "SchemaName": "cdw",
                "CommandFormat": "cdw",
                "DbName": "test",
                "ParentLayerPath": "/HIVE",
                "Description": "test"
            }
        ],
        "ErrorMessage": null,
        "RequestId": "ef431542-96ae-467c-b821-f594df8ac83c"
    }
}
```

