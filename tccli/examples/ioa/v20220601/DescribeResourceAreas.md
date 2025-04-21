**Example 1: 查询资源分组**

查询资源分组

Input: 

```
tccli ioa DescribeResourceAreas --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AreaId": 9,
                    "AreaName": "group1",
                    "Itime": "2023-01-30 10:58:29",
                    "Utime": "2023-04-07 16:35:34"
                },
                {
                    "AreaId": 16,
                    "AreaName": "group2",
                    "Itime": "2023-04-07 16:49:10",
                    "Utime": "2023-04-07 16:50:02"
                }
            ],
            "Page": {
                "PageCount": 0,
                "PageNum": 0,
                "PageSize": 0,
                "Total": 2
            }
        },
        "RequestId": "1777f626-3b13-438c-9490-0cae6fd63db3"
    }
}
```

