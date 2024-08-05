**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPManagerList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --Keyword abc \
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
                    "MNPId": "abc",
                    "MNPIcon": "abc",
                    "MNPName": "abc",
                    "TeamName": "abc",
                    "AccessStatus": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

