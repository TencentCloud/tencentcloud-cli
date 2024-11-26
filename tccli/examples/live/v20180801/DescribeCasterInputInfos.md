**Example 1: 查询输入源列表**



Input: 

```
tccli live DescribeCasterInputInfos --cli-unfold-argument  \
    --CasterId 1234
```

Output: 
```
{
    "Response": {
        "InputInfos": [
            {
                "InputIndex": 1,
                "InputType": 1,
                "InputUrl": "",
                "Description": "点播",
                "PullPushEnable": true,
                "LoopEnable": true,
                "LoopNumber": -1,
                "Volume": 100,
                "InputUrls": [
                    "https://www.example.com/vod.mp4"
                ]
            }
        ],
        "RequestId": "f505e243-8f0e-4d50-a212-bba4effe7bee"
    }
}
```

