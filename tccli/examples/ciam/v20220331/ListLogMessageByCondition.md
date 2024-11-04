**Example 1: 查询日志信息**



Input: 

```
tccli ciam ListLogMessageByCondition --cli-unfold-argument  \
    --UserStoreId 2c3aca3b****************a7efe88e \
    --Pageable.PageSize 10 \
    --Pageable.PageNumber 5 \
    --Filters.0.Key nickname \
    --Filters.0.Values 昵称1 \
    --Filters.0.Logic True \
    --StartTime 1703385600000
```

Output: 
```
{
    "Response": {
        "Total": 100,
        "Pageable": {
            "PageSize": 10,
            "PageNumber": 5
        },
        "Content": [
            {
                "LogId": "a23039fd****************44a78adc",
                "TenantId": "tenantId",
                "UserStoreId": "2c3aca3b****************a7efe88e",
                "EventCode": "FORGET_USERNAME",
                "EventDate": 1703385600000,
                "Description": "忘记用户名日志",
                "Participant": "TENANT",
                "ApplicationClientId": "YmFiZTk5********3ZGZiZmY",
                "ApplicationName": "应用1",
                "AuthSourceId": "5c7df28a********2a3dbbae",
                "AuthSourceName": "账号密码认证源1",
                "AuthSourceType": "USERNAME_PASSWORD",
                "AuthSourceCategory": "UNIVERSAL",
                "Ip": "127.*.*.1",
                "UserAgent": "agent1",
                "UserId": "53e25c3****************e4eb5bd1",
                "Detail": "error detail",
                "ActionResult": "FAIL"
            }
        ],
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

