**Example 1: 用户catalog权限**



Input: 

```
tccli tccatalog DescribeUserPrivilegesSTD --cli-unfold-argument  \
    --Users 700001601851 \
    --ResourceType Catalog
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AuthorityEntity": "Role",
                "Privileges": [
                    "use_schema"
                ],
                "Resource": {
                    "Catalog": "mico_catalog_1031"
                },
                "Role": "weGRole_1300298608_2003"
            }
        ],
        "TotalCount": 2,
        "RequestId": "ebfbd032-b17c-4737-aca6-6c71f03954ae"
    }
}
```

