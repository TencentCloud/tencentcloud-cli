**Example 1: 文件查杀白名单列表**



Input: 

```
tccli tcss DescribeVirusWhiteListRules --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Order DESC \
    --By InsertTime \
    --Filters.0.Name id \
    --Filters.0.Values 246
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 276,
                "ImageCount": 0,
                "ImageIds": [],
                "InsertTime": "2026-04-07T21:53:45+08:00",
                "Md5Count": 1,
                "Md5List": [
                    "923d548dd3c1431d18357da8dffd5780"
                ],
                "Remark": "",
                "Scope": 1,
                "UpdateTime": "2026-04-07T21:53:45+08:00"
            }
        ],
        "TotalCount": 28,
        "RequestId": "d9c3c32e-4e80-48bc-aa00-969b43b16485"
    }
}
```

