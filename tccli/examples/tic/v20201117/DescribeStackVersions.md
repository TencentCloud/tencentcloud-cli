**Example 1: 按照指定的版本ID查询版本详情**



Input: 

```
tccli tic DescribeStackVersions --cli-unfold-argument  \
    --VersionIds ver-zg5pn580 ver-fc7zn57u \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Versions": [
            {
                "VersionId": "ver-zg5pn580",
                "VersionName": "awesome version name",
                "Description": "a nice description",
                "StackId": "stk-hz5vn3te",
                "Status": "VERSION_EDITING",
                "CreateTime": "2020-11-18T07:38:47.330Z"
            },
            {
                "VersionId": "ver-fc7zn57u",
                "VersionName": "awesome version name2",
                "Description": "a nice description2",
                "StackId": "stk-hz5vn3te",
                "Status": "VERSION_EDITING",
                "CreateTime": "2020-11-18T07:38:47.330Z"
            }
        ],
        "RequestId": "8ef5ccb0-4207-468b-bb07-a03e6a772caf"
    }
}
```

**Example 2: 按照名字和状态查询版本列表**



Input: 

```
tccli tic DescribeStackVersions --cli-unfold-argument  \
    --Filters.0.Name Name \
    --Filters.0.Values 'awesome version name' 'awesome version name2' \
    --Filters.1.Name Status \
    --Filters.1.Values VERSION_EDITING \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Versions": [
            {
                "VersionId": "ver-fc7zn57u",
                "VersionName": "awesome version name2",
                "Description": "a nice description2",
                "StackId": "stk-hz5vn3te",
                "Status": "VERSION_EDITING",
                "CreateTime": "2020-11-18T07: 38: 47.330Z"
            }
        ],
        "RequestId": "8ef5ccb0-4207-468b-bb07-a03e6a772caf"
    }
}
```

