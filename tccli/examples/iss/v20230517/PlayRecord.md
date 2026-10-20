**Example 1: 成功**

 

Input: 

```
tccli iss PlayRecord --cli-unfold-argument  \
    --ChannelId c03615ed-fb2a-4c0e-9f53-123456789012 \
    --Start 1791858180 \
    --End 1791858240 \
    --IsInternal False
```

Output: 
```
{
    "Response": {
        "Data": {
            "FMp4": "https://www.demo.cn/live/c03615ed-fb2a-4c0e-9f53-123456789012@675964ad-dd5b-4f5e-af8a-123456789012.live.mp4?start=1791858180&end=1791858240&token=cms_700001111128_1791863756_4uwxnkWB0zCFUhywXjxFPg&type=download",
            "Flv": "https://www.demo.cn/live/live/c03615ed-fb2a-4c0e-9f53-123456789012@675964ad-dd5b-4f5e-af8a-123456789012.live.flv?start=1791858180&end=1791858240&token=cms_700001111128_1791863756_4uwxnkWB0zCFUhywXjxFPg"
        },
        "RequestId": "27c53b3a-4482-4e2e-a1e4-009ef89a372e"
    }
}
```

