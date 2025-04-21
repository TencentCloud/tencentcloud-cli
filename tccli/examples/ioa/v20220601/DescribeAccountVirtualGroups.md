**Example 1: 列表查询用户自定义分组**

列表查询用户自定义分组

Input: 

```
tccli ioa DescribeAccountVirtualGroups --cli-unfold-argument  \
    --Condition.PageSize 100 \
    --Condition.PageNum 1 \
    --Condition.Sort.Field Name \
    --Condition.Sort.Order desc \
    --AccountGroupId 6
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ExtraInfo": "{}",
                    "AccountGroupId": 6,
                    "Itime": "",
                    "Utime": "",
                    "Id": 5,
                    "UserTotal": 0,
                    "Name": "财务",
                    "Description": "",
                    "SourceType": 2
                },
                {
                    "ExtraInfo": "{}",
                    "AccountGroupId": 6,
                    "Itime": "",
                    "Utime": "",
                    "Id": 8,
                    "UserTotal": 0,
                    "Name": "行政",
                    "Description": "",
                    "SourceType": 2
                },
                {
                    "ExtraInfo": "{}",
                    "AccountGroupId": 6,
                    "Itime": "",
                    "Utime": "",
                    "Id": 3,
                    "UserTotal": 5,
                    "Name": "存在产品中心分组",
                    "Description": "",
                    "SourceType": 2
                },
                {
                    "ExtraInfo": "{}",
                    "AccountGroupId": 6,
                    "Itime": "",
                    "Utime": "",
                    "Id": 9,
                    "UserTotal": 1,
                    "Name": "同步测试",
                    "Description": "",
                    "SourceType": 2
                },
                {
                    "ExtraInfo": "{}",
                    "AccountGroupId": 6,
                    "Itime": "",
                    "Utime": "",
                    "Id": 6,
                    "UserTotal": 1,
                    "Name": "iriya",
                    "Description": "",
                    "SourceType": 2
                },
                {
                    "ExtraInfo": "{}",
                    "AccountGroupId": 6,
                    "Itime": "",
                    "Utime": "",
                    "Id": 4,
                    "UserTotal": 0,
                    "Name": "d'd'd'd",
                    "Description": "",
                    "SourceType": 2
                },
                {
                    "ExtraInfo": "{}",
                    "AccountGroupId": 6,
                    "Itime": "",
                    "Utime": "",
                    "Id": 7,
                    "UserTotal": 0,
                    "Name": "666",
                    "Description": "",
                    "SourceType": 2
                }
            ],
            "Page": {
                "PageNum": 1,
                "PageCount": 1,
                "Total": 7,
                "PageSize": 100
            }
        },
        "RequestId": "web-39718972133-1688548231682"
    }
}
```

