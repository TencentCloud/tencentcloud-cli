**Example 1: 视频语义搜索**



Input: 

```
tccli iotexplorer InvokeAISearchService --cli-unfold-argument  \
    --ProductId MVTYMD8YCD \
    --DeviceName dev001 \
    --Query What happened on April 1st
```

Output: 
```
{
    "Response": {
        "RequestId": "a9a9d232-01c0-494a-baa3-57c384463c3f",
        "Summary": "Nine videos captured various scenes on April 1st, showcasing pets eating and playing, a peaceful baby interaction, a resting child, and diligent workers like cleaners and delivery men, all without any safety concerns.",
        "Targets": [
            {
                "ProductId": "MVTYMD8YCD",
                "DeviceName": "dev001",
                "StartTimeMs": 1743456533000,
                "EndTimeMs": 1743456543000,
                "EventId": "alarm",
                "Summary": "Two cats and a dog eating"
            }
        ]
    }
}
```

