**Example 1: DescribeGlobalDomainACL**



Input: 

```
tccli tcmpp DescribeGlobalDomainACL --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --DomainTypes 1 \
    --Keyword  \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 2,
            "DataList": [
                {
                    "DomainId": 5561,
                    "DomainUrl": "openapi.autotest.domain.com",
                    "DomainType": 1,
                    "CreateUser": "800001208871",
                    "CreateTime": "1724223249",
                    "UpdateUser": "800001208871",
                    "UpdateTime": "1724223249"
                },
                {
                    "DomainId": 5440,
                    "DomainUrl": "123132.com",
                    "DomainType": 1,
                    "CreateUser": "jaden",
                    "CreateTime": "1723776362",
                    "UpdateUser": "jaden",
                    "UpdateTime": "1723776362"
                }
            ]
        },
        "RequestId": "e56b6521-bec5-4081-83c5-a6dd9df3a001"
    }
}
```

