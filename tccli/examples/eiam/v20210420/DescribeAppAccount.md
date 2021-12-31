**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeAppAccount --cli-unfold-argument  \
    --SearchCondition.Keyword xx \
    --Limit 0 \
    --Offset 0 \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AppAccountList": {
            "AccountId": "xx",
            "AccountName": "xx",
            "UserList": [
                "xx"
            ],
            "Description": "xx",
            "CreatedDate": "xx"
        },
        "ApplicationId": "xx",
        "RequestId": "xx"
    }
}
```

