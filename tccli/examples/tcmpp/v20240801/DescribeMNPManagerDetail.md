**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPManagerDetail --cli-unfold-argument  \
    --MNPId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "MNPType": "abc",
            "MNPId": "abc",
            "MNPName": "abc",
            "MNPIcon": "abc",
            "MNPIntro": "abc",
            "MNPDesc": "abc",
            "CreateTime": "abc",
            "CreateUser": "abc",
            "AccessStatus": 0,
            "TeamName": "abc",
            "TeamId": "abc"
        },
        "RequestId": "abc"
    }
}
```

