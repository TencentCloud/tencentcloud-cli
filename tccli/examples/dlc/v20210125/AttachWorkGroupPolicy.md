**Example 1: 绑定鉴权策略到工作组**



Input: 

```
tccli dlc AttachWorkGroupPolicy --cli-unfold-argument  \
    --WorkGroupId 112 \
    --PolicySet.0.Table TableName \
    --PolicySet.0.Catalog COSDataCatalog \
    --PolicySet.0.Operation ALL \
    --PolicySet.0.Database DatabaseName
```

Output: 
```
{
    "Response": {
        "RequestId": "0ebb0fdc-0cbd-4408-9f08-ee75a7d6d80f"
    }
}
```

**Example 2: 绑定鉴权策略到工作组（对接TF场景）**



Input: 

```
tccli dlc AttachWorkGroupPolicy --cli-unfold-argument  \
    --WorkGroupId 221683 \
    --PolicySet.0.PolicyType DATABASE \
    --PolicySet.0.Mode COMMON \
    --PolicySet.0.Catalog DataLakeCatalog \
    --PolicySet.0.Database andrew_dlc_02 \
    --PolicySet.0.Table  \
    --PolicySet.0.View  \
    --PolicySet.0.Function  \
    --PolicySet.0.Column  \
    --PolicySet.0.DataEngine  \
    --PolicySet.0.Operation ASSAYER
```

Output: 
```
{
    "Response": {
        "RequestId": "aa6e8c6c-3f6a-4053-a445-36f9065bee28",
        "PolicySet": [
            {
                "Id": 0,
                "PolicyType": "DATABASE",
                "Mode": "COMMON",
                "Catalog": "DataLakeCatalog",
                "Database": "andrew_dlc_02",
                "Table": "",
                "View": "",
                "Function": "",
                "Column": "",
                "DataEngine": "",
                "Operation": "ASSAYER",
                "ReAuth": false,
                "Source": "WORKGROUP",
                "SourceId": 0,
                "SourceName": "",
                "Operator": "700002171047",
                "CreateTime": "",
                "PolicyId": "v1|WORKGROUP|221683|DATABASE|COMMON|DataLakeCatalog|andrew_dlc_02||||||ASSAYER"
            }
        ]
    }
}
```

