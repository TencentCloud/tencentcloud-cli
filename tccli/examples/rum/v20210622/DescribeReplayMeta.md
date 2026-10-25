**Example 1: DescribeReplayMeta示例**



Input: 

```
tccli rum DescribeReplayMeta --cli-unfold-argument  \
    --AppId 146662 \
    --ReplayId daf \
    --SessionId dafa
```

Output: 
```
{
    "Response": {
        "Result": "{\"Platform\":\"unknown\",\"ReplayFormat\":\"rrweb\",\"ReplayId\":\"daf\",\"SegmentCount\":0,\"Segments\":null}",
        "RequestId": "8b4ebd10-d218-4b65-ac72-aca69d8ae2b4"
    }
}
```

