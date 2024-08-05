**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeGlobalDomainList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --DomainTypes 0 \
    --Keyword abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "DomainId": 0,
                    "CustomerID": "abc",
                    "DomainURL": "abc",
                    "DomainType": 0,
                    "CreateUser": "abc",
                    "CreateTime": "abc",
                    "UpdateUser": "abc",
                    "UpdateTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

