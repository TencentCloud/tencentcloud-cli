**Example 1: ModifySampleRate示例**



Input: 

```
tccli rum ModifySampleRate --cli-unfold-argument  \
    --ProjectId 2 \
    --SampleRate 99.9
```

Output: 
```
{
    "Response": {
        "Result": "{\"ProjectId\":2,\"SampleRate\":99.9,\"UpdatedAt\":\"2026-04-14T13:53:36.672+08:00\"}",
        "RequestId": "1b67da78-db46-4c1a-9394-65dd85404b35"
    }
}
```

