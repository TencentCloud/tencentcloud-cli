**Example 1: 获取查询视图列表**



Input: 

```
tccli cls DescribeSearchViews --cli-unfold-argument  \
    --Filters.0.Key logsetId \
    --Filters.0.Values 9ec1f40f-7bca-4da8-bbd0-29b358a1ba2a
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "CreateTime": 1776912487,
                "LogsetId": "9ec1f40f-7bca-4da8-bbd0-29b358a1ba2a",
                "LogsetRegion": "ap-**************",
                "Topics": [
                    {
                        "LogsetId": "9ec1f40f-7bca-4da8-bbd0-29b358a1ba2a",
                        "Region": "ap-**************",
                        "TopicId": "k****-5-1254139626"
                    }
                ],
                "UpdateTime": 1776912487,
                "ViewId": "k****-search-4-view",
                "ViewName": "k****-search-4",
                "ViewType": "log"
            }
        ],
        "Total": 4,
        "RequestId": "7090fbf8-4000-4712-992f-3a2d7816b702"
    }
}
```

