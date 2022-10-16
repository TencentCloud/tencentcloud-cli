**Example 1: 查询全量函数（层级化）接口**



Input: 

```
tccli wedata DescribeOrganizationalFunctions --cli-unfold-argument  \
    --ProjectId xx \
    --Type xx \
    --Name xx \
    --DisplayName xx
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Category": "xx",
                "Status": "xx",
                "Kind": "xx",
                "DisplayName": "xx",
                "Name": "xx",
                "OwnerUserIds": [
                    0
                ],
                "ReturnDesc": "xx",
                "FuncId": "xx",
                "ParamDesc": "xx",
                "Example": "xx",
                "ClassName": "xx",
                "ResourceList": [
                    {
                        "Comment": "xx",
                        "UserName": "xx",
                        "Timestamp": "xx",
                        "UserId": "xx",
                        "Content": "xx",
                        "Tag": "xx",
                        "Type": "xx"
                    }
                ],
                "OperatorUserIds": [
                    0
                ],
                "Usage": "xx",
                "ClusterIdentifier": "xx",
                "LayerPath": "xx",
                "Type": "xx",
                "ParentLayerPath": "xx",
                "Description": "xx"
            }
        ],
        "ErrorMessage": "xx",
        "RequestId": "xx"
    }
}
```

