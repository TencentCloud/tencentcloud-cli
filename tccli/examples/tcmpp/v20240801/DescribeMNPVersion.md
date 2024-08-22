**Example 1: DescribeMNPVersion**



Input: 

```
tccli tcmpp DescribeMNPVersion --cli-unfold-argument  \
    --BusinessId 2024082016302581955 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "MNPId": "mpg9yjc0qbpkelik",
            "TaskId": "2024082016302581955",
            "TaskStatus": 60,
            "TaskMsg": "成功"
        },
        "RequestId": "2a2e7e38-f18e-411b-9e09-24ab881c3b60"
    }
}
```

