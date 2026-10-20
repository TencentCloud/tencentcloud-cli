**Example 1: 请求示例**



Input: 

```
tccli live DescribeStreamPackageOutputStatistics --cli-unfold-argument  \
    --StartTime 2026-08-24T00:00:00+08:00 \
    --EndTime 2026-08-25T12:00:00+08:00 \
    --Types LiveChannel \
    --Dimension False \
    --Granularity 5
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "ChannelId": "/v1/019fcbc0910a1eb828202c302ebdb8",
                "Output": 506988117,
                "Type": "LiveChannel"
            }
        ],
        "TotalOutput": 8150075538,
        "RequestId": "a987670e-11fb-41e1-a060-ceb09d2a9a51"
    }
}
```

