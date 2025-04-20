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

