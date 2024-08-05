**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeUserList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --Keyword abc \
    --AccountType 0 \
    --TeamId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "UserId": "abc",
                    "UserAccount": "abc",
                    "Teams": "abc",
                    "AccountType": 0,
                    "UserName": "abc",
                    "CreateTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

