**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeDomainTeamList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
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
                    "TeamId": "abc",
                    "TeamName": "abc",
                    "CreateUser": "abc",
                    "CreateTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

