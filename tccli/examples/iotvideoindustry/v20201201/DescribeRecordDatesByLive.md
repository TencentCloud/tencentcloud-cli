**Example 1: 直播录像存储日期列表**



Input: 

```
tccli iotvideoindustry DescribeRecordDatesByLive --cli-unfold-argument  \
    --LiveChannelId cea6f74f29164253b43411fd888f4dc3 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Dates": [
            "2021-09-07"
        ],
        "RequestId": "fd344df8-6121-4e75-b417-383a67268354111"
    }
}
```

