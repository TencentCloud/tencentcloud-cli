**Example 1: 查询事件排行**



Input: 

```
tccli rum DescribeTDEMEventRank --cli-unfold-argument  \
    --AppId 7 \
    --StartTime 1787404860000 \
    --EndTime 1789996860000 \
    --Kind api
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Count": 70,
                "Duration": 458.09171540396557,
                "URL": "https:******************************************"
            }
        ],
        "RequestId": "41829edb-5f4e-43d1-9afa-9ce22fa55f3e"
    }
}
```

**Example 2: 查询异常维度完整分类与包含项**

按精确半开时间窗查询Web OS异常分布，返回完整主项、0计数及页面不存在包含项；主项计总，包含项不重复计总。

Input: 

```
tccli rum DescribeTDEMEventRank --cli-unfold-argument  \
    --AppId 17 \
    --StartTime 1789660800000 \
    --EndTime 1792252800000 \
    --Kind exception_dimension \
    --GroupBy os \
    --ProjectType web \
    --CategoryKeys js_error promise_error api_error.http api_error.business resource_error.script resource_error.image resource_error.stylesheet resource_error.media resource_error.lazy_load blank_screen log.report js_error.page_not_found \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "ExceptionDistribution": {
            "Rows": [
                {
                    "Items": [
                        {
                            "Count": 51,
                            "IncludedInTotal": true,
                            "Key": "js_error"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": false,
                            "Key": "js_error.page_not_found",
                            "ParentKey": "js_error"
                        },
                        {
                            "Count": 49,
                            "IncludedInTotal": true,
                            "Key": "promise_error"
                        },
                        {
                            "Count": 282,
                            "IncludedInTotal": true,
                            "Key": "api_error.http"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": true,
                            "Key": "api_error.business"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": true,
                            "Key": "resource_error.script"
                        },
                        {
                            "Count": 54,
                            "IncludedInTotal": true,
                            "Key": "resource_error.image"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": true,
                            "Key": "resource_error.stylesheet"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": true,
                            "Key": "resource_error.media"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": true,
                            "Key": "resource_error.lazy_load"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": true,
                            "Key": "blank_screen"
                        },
                        {
                            "Count": 0,
                            "IncludedInTotal": true,
                            "Key": "log.report"
                        }
                    ],
                    "RowKey": "exd1.b3JkaW5hcnk6d2Vi.b3M.TWFjIE9TIFg",
                    "TotalCount": 436,
                    "Value": "Mac OS X"
                }
            ]
        },
        "Items": [],
        "RequestId": "1095ed90-eb47-4bc0-a9c1-a038dbae5f90"
    }
}
```

