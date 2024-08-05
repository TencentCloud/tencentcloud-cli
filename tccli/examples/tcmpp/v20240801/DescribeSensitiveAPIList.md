**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeSensitiveAPIList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --Keyword abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "ApiId": "abc",
                    "ApiName": "abc",
                    "ApiMethod": "abc",
                    "ApiDesc": "abc",
                    "CreateUser": "abc",
                    "CreateTime": "abc",
                    "UpdateUser": "abc",
                    "UpdateTime": "abc",
                    "APIType": 1,
                    "Status": 1
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

