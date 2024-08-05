**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeOnlineVersion --cli-unfold-argument  \
    --MNPId abc \
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
                    "MNPId": "abc",
                    "MNPVersion": "abc",
                    "MNPVersionId": 0,
                    "MNPVersionNote": "abc",
                    "UpdateTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

