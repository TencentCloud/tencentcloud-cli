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

**Example 2: 错误用例**

错误用例

Input: 

```
tccli wedata DescribeOrganizationalFunctions --cli-unfold-argument  \
    --Type 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "当前用户角色或WeData版本没有权限，请进行角色授权或者升级WeData版本"
        },
        "RequestId": "da268a37-2a3f-469f-afea-d41cd01d6a7c"
    }
}
```

