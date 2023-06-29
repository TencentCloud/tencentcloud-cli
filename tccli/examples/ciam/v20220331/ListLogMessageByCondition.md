**Example 1: 查询日志信息**



Input: 

```
tccli ciam ListLogMessageByCondition --cli-unfold-argument  \
    --UserStoreId xx \
    --StartTime 0 \
    --Pageable.PageNumber 0 \
    --Pageable.PageSize 0 \
    --Filters.0.Values xx \
    --Filters.0.Key xx \
    --Filters.0.Logic True
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "UserStoreId": "xx",
                "ApplicationName": "xx",
                "Participant": "xx",
                "Description": "xx",
                "EventCode": "xx",
                "Ip": "xx",
                "ApplicationClientId": "xx",
                "UserId": "xx",
                "Detail": "xx",
                "AuthSourceName": "xx",
                "TenantId": "xx",
                "LogId": "xx",
                "AuthSourceId": "xx",
                "AuthSourceType": "xx",
                "UserAgent": "xx",
                "AuthSourceCategory": "xx",
                "EventDate": 0
            }
        ],
        "Total": 0,
        "Pageable": {
            "PageNumber": 0,
            "PageSize": 0
        },
        "RequestId": "xx"
    }
}
```

