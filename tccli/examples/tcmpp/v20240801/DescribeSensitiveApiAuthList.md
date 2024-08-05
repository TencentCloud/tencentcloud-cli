**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeSensitiveApiAuthList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --MNPId abc \
    --PlatformId abc \
    --ApplicationId abc \
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
                    "APIId": "abc",
                    "APIName": "abc",
                    "APIMethod": "abc",
                    "APIStatus": 0,
                    "APIApplyStatus": 0,
                    "RejectReason": "abc",
                    "APIDesc": "desc",
                    "APIType": 1
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

