**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeSimpleApplicationInfoList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --PlatformId abc \
    --Keyword abc \
    --LoadAssistantApp True \
    --MNPId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "ApplicationID": "abc",
                    "AppIdentityID": 0,
                    "ApplicationName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

