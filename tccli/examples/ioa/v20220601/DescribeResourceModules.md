**Example 1: 分页获取资源模块**



Input: 

```
tccli ioa DescribeResourceModules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 10,
                "PageNum": 0,
                "Total": 1,
                "PageCount": 1
            },
            "Items": [
                {
                    "EnableFlag": 1,
                    "Itime": "2022-07-21 10:24:41",
                    "Utime": "2022-07-21 10:24:41",
                    "DomainId": 1,
                    "AreaId": 109,
                    "AreaName": "11"
                }
            ]
        },
        "RequestId": "1658370316.5893214"
    }
}
```

**Example 2: 搜索业务资源模块**



Input: 

```
tccli ioa DescribeResourceModules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 10,
                "PageNum": 0,
                "Total": 1,
                "PageCount": 1
            },
            "Items": [
                {
                    "EnableFlag": 1,
                    "Itime": "2022-07-21 10:24:41",
                    "Utime": "2022-07-21 10:24:41",
                    "DomainId": 1,
                    "AreaId": 109,
                    "AreaName": "资源"
                }
            ]
        },
        "RequestId": "1658370316.5893214"
    }
}
```

