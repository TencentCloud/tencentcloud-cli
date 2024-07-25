**Example 1: DEMO**



Input: 

```
tccli tcmpp DescribeGlobalDomainList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --DomainTypes 0 \
    --Keyword abc \
    --GlobalTeamId abc
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

