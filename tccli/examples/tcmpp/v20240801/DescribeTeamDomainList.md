**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeTeamDomainList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --TeamId abc \
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
                    "DomainId": 0,
                    "MNPId": "abc",
                    "MNPName": "abc",
                    "DomainUrl": "abc",
                    "DomainType": 0,
                    "Status": 0,
                    "CreateUser": "abc",
                    "CreateTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

