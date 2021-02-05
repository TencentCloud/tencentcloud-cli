**Example 1: DescribeLoRaFrequency**

获取LoRa自定义频点详情

Input: 

```
tccli iotexplorer DescribeLoRaFrequency --cli-unfold-argument  \
    --FreqId 0cdd67ed-c198-403f-a2b7-043e09c7639d
```

Output: 
```
{
    "Response": {
        "Data": {
            "FreqId": "0cdd67ed-c198-403f-a2b7-043e09c7639d",
            "FreqName": "F1",
            "Description": "",
            "ChannelsDataUp": [
                486300000
            ],
            "ChannelsDataRX1": [
                486300000
            ],
            "ChannelsDataRX2": [
                486300000
            ],
            "ChannelsJoinUp": [
                486300000
            ],
            "ChannelsJoinRX1": [
                486300000
            ],
            "ChannelsJoinRX2": [
                486300000
            ],
            "CreateTime": 1600859096
        },
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

