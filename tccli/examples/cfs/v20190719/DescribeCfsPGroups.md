**Example 1: 查询权限组列表**



Input: 

```
tccli cfs DescribeCfsPGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PGroupList": [
            {
                "BindCfsNum": 7,
                "CDate": "2017-06-21 17:30:05",
                "DescInfo": "默认权限组",
                "Name": "默认权限组",
                "PGroupId": "pgroupbasic"
            }
        ],
        "RequestId": "7a533ad4-7d11-4a67-87a9-b02891475647"
    }
}
```

