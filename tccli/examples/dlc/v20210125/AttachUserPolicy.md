**Example 1: 绑定鉴权策略到用户**



Input: 

```
tccli dlc AttachUserPolicy --cli-unfold-argument  \
    --UserId 10401463674518 \
    --PolicySet.0.Database create_test \
    --PolicySet.0.Catalog DataLakeCatalog \
    --PolicySet.0.Operation CREATE_TABLE \
    --PolicySet.0.Table test_table \
    --PolicySet.0.PolicyType TABLE \
    --PolicySet.0.Mode SENIOR
```

Output: 
```
{
    "Response": {
        "RequestId": "4e2a0b4b-6c0b-40de-9e39-0761ed1f6be4"
    }
}
```

**Example 2: 绑定鉴权策略到用户（TF场景）**



Input: 

```
tccli dlc AttachUserPolicy --cli-unfold-argument  \
    --UserId 700002810925 \
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
        "RequestId": "915bb9e6-9194-4bb7-81ff-c31f8d7bc792",
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
                "Source": "USER",
                "SourceId": 0,
                "SourceName": "",
                "Operator": "700002171047",
                "CreateTime": "",
                "PolicyId": "v1|USER|700002810925|DATABASE|COMMON|DataLakeCatalog|andrew_dlc_02||||||ASSAYER"
            }
        ]
    }
}
```

