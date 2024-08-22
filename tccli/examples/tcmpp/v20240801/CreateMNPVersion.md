**Example 1: CreateMNPVersion**



Input: 

```
tccli tcmpp CreateMNPVersion --cli-unfold-argument  \
    --MNPId mpg9yjc0qbpkelik \
    --MNPVersion 1.0.278 \
    --FileUrl http://127.0.0.1/T04257DS9431720WTAG/console/20240820163023-86c669ca06.zip \
    --MNPVersionIntro autotest_create \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "2024082016302581955"
        },
        "RequestId": "b7bbff2d-fea5-471e-918f-c9684abf2fd3"
    }
}
```

