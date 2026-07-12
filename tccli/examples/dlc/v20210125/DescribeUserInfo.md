**Example 1: test**



Input: 

```
tccli dlc DescribeUserInfo --cli-unfold-argument  \
    --UserId 1**********7 \
    --Type DataAuth \
    --Filters.0.Name policy-type \
    --Filters.0.Values TABLE \
    --SortBy create-time \
    --Sorting desc \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-1507fd716595",
        "UserInfo": {
            "AccountType": "UserAccount",
            "CatalogPolicyInfo": null,
            "DataPolicyInfo": {
                "PolicySet": [
                    {
                        "Catalog": "DataLakeCatalog",
                        "Database": "database1",
                        "Id": 398710,
                        "Mode": "SENIOR",
                        "Operation": "ALL",
                        "Operator": "Owner",
                        "PolicyType": "TABLE",
                        "ReAuth": true,
                        "Source": "USER",
                        "Table": "table1",
                        "Column": null,
                        "Function": null,
                        "CreateTime": null,
                        "SourceId": null,
                        "SourceName": null,
                        "View": null,
                        "DataEngine": null
                    }
                ],
                "TotalCount": 1
            },
            "EnginePolicyInfo": {
                "PolicySet": null,
                "TotalCount": 0
            },
            "RowFilterInfo": {
                "PolicySet": null,
                "TotalCount": 0
            },
            "Type": "DataAuth",
            "UserAlias": "1**********7",
            "UserDescription": "Owner",
            "UserId": "1**********7",
            "UserType": "ADMIN",
            "WorkGroupInfo": {
                "TotalCount": 0,
                "WorkGroupSet": null
            }
        }
    }
}
```

**Example 2: test（TF场景）**



Input: 

```
tccli dlc DescribeUserInfo --cli-unfold-argument  \
    --UserId 700002810925 \
    --Type DataAuth \
    --PolicyId v1|USER|700002810925|DATABASE|COMMON|DataLakeCatalog|t0_lotuss||||||ASSAYER
```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "AccountType": "UserAccount",
            "CatalogPolicyInfo": {
                "PolicySet": [],
                "TotalCount": 0
            },
            "DataPolicyInfo": {
                "PolicySet": [
                    {
                        "Catalog": "DataLakeCatalog",
                        "Column": "",
                        "CreateTime": "",
                        "DataEngine": "",
                        "Database": "t0_lotuss",
                        "Function": "",
                        "Id": 797338,
                        "Mode": "COMMON",
                        "Operation": "ASSAYER",
                        "Operator": "700002171047",
                        "PolicyId": "v1|USER|700002810925|DATABASE|COMMON|DataLakeCatalog|t0_lotuss||||||ASSAYER",
                        "PolicyType": "DATABASE",
                        "ReAuth": false,
                        "Source": "USER",
                        "SourceId": 0,
                        "SourceName": "",
                        "Table": "",
                        "View": ""
                    }
                ],
                "TotalCount": 1
            },
            "EnginePolicyInfo": {
                "PolicySet": [],
                "TotalCount": 0
            },
            "ModelPolicyInfo": {
                "PolicySet": [],
                "TotalCount": 0
            },
            "RowFilterInfo": {
                "PolicySet": [],
                "TotalCount": 0
            },
            "Type": "DataAuth",
            "UserAlias": "test-tf",
            "UserDescription": "测试用户",
            "UserId": "700002810925",
            "UserType": "COMMON",
            "WorkGroupInfo": {
                "TotalCount": 0,
                "WorkGroupSet": null
            }
        },
        "RequestId": "4f710e03-5c67-4e2e-b93f-983a33855159"
    }
}
```

