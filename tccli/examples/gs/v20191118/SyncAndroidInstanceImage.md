**Example 1: SyncAndroidInstanceImage 示例**



Input: 

```
tccli gs SyncAndroidInstanceImage --cli-unfold-argument  \
    --AndroidInstanceImageId image-abcd1234 \
    --DestinationZones ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "SyncAndroidInstanceImages": [
            {
                "AndroidInstanceImageId": "image-49va6apu",
                "AndroidInstanceImageZone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "requestid"
    }
}
```

