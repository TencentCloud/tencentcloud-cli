**Example 1: 获取域名的自定义线路分组列表**

获取域名的自定义线路分组列表

Input: 

```
tccli dnspod DescribeLineGroupList --cli-unfold-argument  \
    --Domain dnspod.cn \
    --Offset 0 \
    --Length 20 \
    --SortType desc
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "LineGroups": [
            {
                "Id": 9,
                "DomainId": 1005,
                "Name": "group06",
                "Lines": [
                    "必应"
                ],
                "CreatedOn": "2021-11-18 16:45:15",
                "UpdatedOn": "2021-11-19 10:55:13"
            },
            {
                "Id": 8,
                "DomainId": 1005,
                "Name": "group04",
                "Lines": [
                    "搜索引擎"
                ],
                "CreatedOn": "2021-11-18 16:43:36",
                "UpdatedOn": "2021-11-18 16:43:36"
            },
            {
                "Id": 7,
                "DomainId": 1005,
                "Name": "group03",
                "Lines": [
                    "联通",
                    "教育网"
                ],
                "CreatedOn": "2021-11-18 16:42:36",
                "UpdatedOn": "2021-11-18 16:42:36"
            },
            {
                "Id": 6,
                "DomainId": 1005,
                "Name": "group02",
                "Lines": [
                    "电信",
                    "移动"
                ],
                "CreatedOn": "2021-11-18 16:42:05",
                "UpdatedOn": "2021-11-18 16:42:05"
            },
            {
                "Id": 5,
                "DomainId": 1005,
                "Name": "group01",
                "Lines": [
                    "百度",
                    "谷歌"
                ],
                "CreatedOn": "2021-11-18 16:41:19",
                "UpdatedOn": "2021-11-18 16:41:19"
            }
        ],
        "Info": {
            "NowTotal": 5,
            "Total": 5,
            "AvailableCount": 0
        }
    }
}
```

