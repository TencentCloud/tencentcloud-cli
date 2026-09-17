**Example 1: 成功示例**



Input: 

```
tccli iotexplorer GetVodCloudStorageVideoList --cli-unfold-argument  \
    --ProductId YYZRTPMCUG \
    --DeviceName *******_test_7 \
    --Date 2026-08-26 \
    --ChannelId 23
```

Output: 
```
{
    "Response": {
        "Context": "",
        "Listover": true,
        "VideoList": [
            {
                "EndTime": 1787729122,
                "FileId": "5001834817655768113",
                "Psign": "",
                "StartTime": 1787729072,
                "StreamType": "vod",
                "Url": "https://1500058999.vod-qcloud.com/fe0388edvodgzp1500058999/02dbb5c45001834817655768113/1Nh4Vbiish0A.m3u8?sign=6de370a61cfbec60c49269911552c865&t=6a8ef0c4&us=178774544425833604633398685843586842504412"
            }
        ],
        "VodAppId": "1500058***",
        "RequestId": "9ba1e7f3-55b0-4d06-a77a-e2451f71a915"
    }
}
```

