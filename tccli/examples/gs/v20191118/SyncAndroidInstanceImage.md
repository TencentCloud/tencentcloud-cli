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
                "AndroidInstanceImageId": "abc",
                "AndroidInstanceImageZone": "abc"
            }
        ],
        "RequestId": "requestid"
    }
}
```

