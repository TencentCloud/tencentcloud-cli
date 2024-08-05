**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPBoard --cli-unfold-argument  \
    --MNPId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "MNPId": "abc",
                "MNPVersionId": 0,
                "MNPName": "abc",
                "MNPIcon": "abc",
                "MNPType": "abc",
                "MNPIntro": "abc",
                "MNPDesc": "abc",
                "CreateUser": "abc",
                "CreateTime": "abc",
                "MNPVersion": "abc",
                "MNPVersionIntro": "abc",
                "Phase": "abc",
                "AuditStatus": 0,
                "AuditNo": "abc",
                "ShowCase": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

