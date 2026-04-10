**Example 1: 查询项目列表**



Input: 

```
tccli omics DescribeProjects --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name Region \
    --Filters.0.Values ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Projects": [
            {
                "CreateTime": "2023-10-25 20:17:58",
                "Creator": "",
                "Description": "2",
                "IsDefault": true,
                "Name": "demo project for testing",
                "ProjectId": "prj-wide-cerulean-cicadia-967487",
                "Region": "ap-guangzhou",
                "UpdateTime": "2025-12-11 16:08:17"
            }
        ],
        "TotalCount": 108,
        "RequestId": "bdd774c2-8fa3-47f8-b17a-89792cc5126a"
    }
}
```

