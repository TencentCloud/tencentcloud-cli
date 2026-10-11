**Example 1: 列表查询用户自定义分组**

列表查询用户自定义分组

Input: 

```
tccli ioa DescribeAccountVirtualGroups --cli-unfold-argument  \
    --AccountGroupId 1099
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccountGroupId": 1099,
                    "Description": "",
                    "ExtraInfo": "{******************}",
                    "Id": 528,
                    "Itime": "",
                    "Name": "ioa",
                    "SourceType": 2,
                    "UserTotal": 11,
                    "Utime": ""
                }
            ],
            "Page": {
                "PageCount": 6,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 58
            }
        },
        "RequestId": "8244ba70-3700-4608-b2bb-8843a801cb3c"
    }
}
```

