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

