**Example 1: 获取预置位列表**



Input: 

```
tccli iotvideoindustry DescribePresetList --cli-unfold-argument  \
    --ChannelId 99576636581320000278_99576636581320000278 \
    --DeviceId 99576636581320000278_99576636581320000278
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "PresetId": 8,
                "PresetName": "房门",
                "Status": 1,
                "ResetTime": 10
            }
        ],
        "RequestId": "20e4eb35-5429-4b25-8e4e-d7435518f194"
    }
}
```

