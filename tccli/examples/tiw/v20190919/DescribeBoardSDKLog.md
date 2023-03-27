**Example 1: 查询白板日志**



Input: 

```
tccli tiw DescribeBoardSDKLog --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 73394291 \
    --UserId tic_web \
    --TimeRange 1614519034000 1614691834999 \
    --Context  \
    --AggregationInterval 1h \
    --Query  \
    --Ascending True
```

Output: 
```
{
    "Response": {
        "RequestId": "52214ab1-eeaa-4c9a-aa8f-6c501f7cae18",
        "Total": 65,
        "Context": "",
        "Sources": [],
        "Buckets": []
    }
}
```

