**Example 1: 视频通道码率信息返回结果**

正常响应

Input: 

```
tccli iss DescribeVideoBitRate --cli-unfold-argument  \
    --ChannelIds ffefbe2f-****-4659-****-7596****3900 ffd2****-a057-****-a3dc-91b1****cbc0
```

Output: 
```
{
    "Response": {
        "Data": {
            "BitRates": [
                {
                    "ChannelId": "ffefbe2f-****-4659-****-7596****3900",
                    "Bitrate": 15.23
                },
                {
                    "ChannelId": "ffd2****-a057-****-a3dc-91b1****cbc0",
                    "Bitrate": 3.23
                }
            ]
        },
        "RequestId": "e4a15dcd-****-4804-****-2187ac35fe1d"
    }
}
```

