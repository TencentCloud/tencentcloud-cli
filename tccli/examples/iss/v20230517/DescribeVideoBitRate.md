**Example 1: 视频通道码率信息返回结果**

正常响应

Input: 

```
tccli iss DescribeVideoBitRate --cli-unfold-argument  \
    --ChannelIds ffefbe2f-a5a2-4659-a56f-7596a0e13900 ffd25236-a057-4c30-a3dc-91b1aee8cbc0
```

Output: 
```
{
    "Response": {
        "Data": {
            "BitRates": [
                {
                    "ChannelId": "ffefbe2f-a5a2-4659-a56f-7596a0e13900",
                    "Bitrate": 15.23
                },
                {
                    "ChannelId": "ffd25236-a057-4c30-a3dc-91b1aee8cbc0",
                    "Bitrate": 3.23
                }
            ]
        },
        "RequestId": "e4a15dcd-b66b-4804-a4b0-2187ac35fe1d"
    }
}
```

