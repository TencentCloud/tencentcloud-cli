**Example 1: 查询token统计日志**



Input: 

```
tccli apis DescribeTokenLogs --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --StartTime 1764518400000 \
    --EndTime 1767196799999
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "Sum": {
                "ReqCount": 0,
                "ReqTokens": 0,
                "ResTokens": 0,
                "TotalTokens": 0
            }
        },
        "RequestId": "450c8c76-187d-4ed5-b2c0-5bc9b8f36480"
    }
}
```

