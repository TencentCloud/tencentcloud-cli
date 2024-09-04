**Example 1: test**



Input: 

```
tccli dlc DescribeUserInfo --cli-unfold-argument  \
    --UserId abc \
    --Type abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --SortBy abc \
    --Sorting abc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "UserId": "abc",
            "Type": "abc",
            "UserType": "abc",
            "UserDescription": "abc",
            "DataPolicyInfo": {
                "PolicySet": [
                    {
                        "Database": "abc",
                        "Catalog": "abc",
                        "Table": "abc",
                        "Operation": "abc",
                        "PolicyType": "abc",
                        "Function": "abc",
                        "View": "abc",
                        "Column": "abc",
                        "DataEngine": "abc",
                        "ReAuth": true,
                        "Source": "abc",
                        "Mode": "abc",
                        "Operator": "abc",
                        "CreateTime": "abc",
                        "SourceId": 0,
                        "SourceName": "abc",
                        "Id": 0
                    }
                ],
                "TotalCount": 0
            },
            "EnginePolicyInfo": {
                "PolicySet": [
                    {
                        "Database": "abc",
                        "Catalog": "abc",
                        "Table": "abc",
                        "Operation": "abc",
                        "PolicyType": "abc",
                        "Function": "abc",
                        "View": "abc",
                        "Column": "abc",
                        "DataEngine": "abc",
                        "ReAuth": true,
                        "Source": "abc",
                        "Mode": "abc",
                        "Operator": "abc",
                        "CreateTime": "abc",
                        "SourceId": 0,
                        "SourceName": "abc",
                        "Id": 0
                    }
                ],
                "TotalCount": 0
            },
            "WorkGroupInfo": {
                "WorkGroupSet": [
                    {
                        "WorkGroupId": 0,
                        "WorkGroupName": "abc",
                        "WorkGroupDescription": "abc",
                        "Creator": "abc",
                        "CreateTime": "abc"
                    }
                ],
                "TotalCount": 0
            },
            "UserAlias": "abc",
            "RowFilterInfo": {
                "PolicySet": [
                    {
                        "Database": "abc",
                        "Catalog": "abc",
                        "Table": "abc",
                        "Operation": "abc",
                        "PolicyType": "abc",
                        "Function": "abc",
                        "View": "abc",
                        "Column": "abc",
                        "DataEngine": "abc",
                        "ReAuth": true,
                        "Source": "abc",
                        "Mode": "abc",
                        "Operator": "abc",
                        "CreateTime": "abc",
                        "SourceId": 0,
                        "SourceName": "abc",
                        "Id": 0
                    }
                ],
                "TotalCount": 0
            }
        },
        "RequestId": "abc"
    }
}
```

