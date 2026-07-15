**Example 1: 获取工作组详细信息**



Input: 

```
tccli dlc DescribeWorkGroupInfo --cli-unfold-argument  \
    --WorkGroupId 63304 \
    --Type User \
    --Filters.0.Name policy-source \
    --Filters.0.Values WORKGROUP \
    --SortBy create-time \
    --Sorting desc \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "WorkGroupInfo": {
            "WorkGroupId": 12,
            "UserInfo": {
                "TotalCount": 1,
                "UserSet": [
                    {
                        "UserDescription": "default description",
                        "UserAlias": "testname",
                        "UserId": "12319087121",
                        "CreateTime": "2011-11-23 11:32:42",
                        "Creator": "12319087121"
                    }
                ]
            },
            "WorkGroupName": "testGroup",
            "RowFilterInfo": null,
            "DataPolicyInfo": null,
            "EnginePolicyInfo": null,
            "WorkGroupDescription": "default workgroup",
            "Type": "User"
        },
        "RequestId": "gsdf-213kjs9sf-f11fafsaf-12e1k"
    }
}
```

**Example 2: 获取工作组详细信息（TF场景）**



Input: 

```
tccli dlc DescribeWorkGroupInfo --cli-unfold-argument  \
    --WorkGroupId 221683 \
    --Type DataAuth \
    --PolicyId v1|WORKGROUP|221683|DATABASE|COMMON|DataLakeCatalog|andrew_dlc_02||||||ASSAYER
```

Output: 
```
{
    "Response": {
        "RequestId": "506388b2-aa19-4c1f-97a1-f7e6add6a1c1",
        "WorkGroupInfo": {
            "WorkGroupId": 221683,
            "WorkGroupName": "test_0710",
            "WorkGroupDescription": "",
            "Type": "DataAuth",
            "UserInfo": {
                "UserSet": [],
                "TotalCount": 0
            },
            "DataPolicyInfo": {
                "PolicySet": [
                    {
                        "Id": 797339,
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
                        "SourceId": 221683,
                        "SourceName": "",
                        "Operator": "700002171047",
                        "CreateTime": "",
                        "PolicyId": "v1|WORKGROUP|221683|DATABASE|COMMON|DataLakeCatalog|andrew_dlc_02||||||ASSAYER"
                    }
                ],
                "TotalCount": 1
            },
            "EnginePolicyInfo": {
                "PolicySet": [
                    {
                        "Id": 0,
                        "PolicyType": "",
                        "Mode": "",
                        "Catalog": "",
                        "Database": "",
                        "Table": "",
                        "View": "",
                        "Function": "",
                        "Column": "",
                        "DataEngine": "",
                        "Operation": "",
                        "ReAuth": false,
                        "Source": "",
                        "SourceId": 0,
                        "SourceName": "",
                        "Operator": "",
                        "CreateTime": ""
                    }
                ],
                "TotalCount": 0
            },
            "RowFilterInfo": {
                "PolicySet": [
                    {
                        "Id": 0,
                        "PolicyType": "",
                        "Mode": "",
                        "Catalog": "",
                        "Database": "",
                        "Table": "",
                        "View": "",
                        "Function": "",
                        "Column": "",
                        "DataEngine": "",
                        "Operation": "",
                        "ReAuth": false,
                        "Source": "",
                        "SourceId": 0,
                        "SourceName": "",
                        "Operator": "",
                        "CreateTime": ""
                    }
                ],
                "TotalCount": 0
            }
        }
    }
}
```

