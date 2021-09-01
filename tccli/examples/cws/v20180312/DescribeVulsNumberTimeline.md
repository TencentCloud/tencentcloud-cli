**Example 1: 查看漏洞数随时间变化统计信息**

本接口 (DescribeVulsNumberTimeline) 用于查询漏洞数随时间变化统计信息

Input: 

```
tccli cws DescribeVulsNumberTimeline --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "33e45f0e-f971-4784-ab50-e8205e995355",
        "TotalCount": 2,
        "VulsTimeline": [
            {
                "Appid": 1251001047,
                "CreatedAt": "2018-06-12T22:25:00+08:00",
                "Date": "2018-06-11T00:00:00+08:00",
                "Id": 1,
                "ImpactSiteNum": 1,
                "PageCount": 33,
                "SiteNum": 8,
                "UpdatedAt": "2018-06-12T22:25:00+08:00",
                "VulsHighNum": 8,
                "VulsLowNum": 0,
                "VulsMiddleNum": 2,
                "VulsNoticeNum": 0
            },
            {
                "Appid": 1251001047,
                "CreatedAt": "2018-06-13T17:54:41.418296+08:00",
                "Date": "2018-06-13T00:00:00+08:00",
                "Id": 0,
                "ImpactSiteNum": 1,
                "PageCount": 33,
                "SiteNum": 8,
                "UpdatedAt": "2018-06-13T17:54:41.418298+08:00",
                "VulsHighNum": 8,
                "VulsLowNum": 0,
                "VulsMiddleNum": 2,
                "VulsNoticeNum": 0
            }
        ]
    }
}
```

