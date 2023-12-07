**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPDetail --cli-unfold-argument  \
    --Id 0 \
    --MNPId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 0,
            "MNPType": "abc",
            "MNPId": "abc",
            "MNPName": "abc",
            "MNPIcon": "abc",
            "MNPIntro": "abc",
            "MNPDesc": "abc",
            "CreateUser": "abc",
            "CreateTime": 0,
            "OnlineStatus": 0,
            "Applications": [
                {
                    "ApplicationId": "abc",
                    "ApplicationName": "abc"
                }
            ],
            "Tags": [
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

