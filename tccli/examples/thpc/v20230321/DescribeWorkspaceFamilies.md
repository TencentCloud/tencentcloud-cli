**Example 1: 查询HYBRID类别的规格族**

查询HYBRID（算力互联）类别下有哪些规格族

Input: 

```
tccli thpc DescribeWorkspaceFamilies --cli-unfold-argument  \
    --Filters.0.Name workspace-class \
    --Filters.0.Values HYBRID
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "WorkspaceFamilySet": [
            {
                "SpaceFamily": "64DZZ",
                "SpaceClass": "HYBRID"
            }
        ],
        "TotalCount": 1
    }
}
```

