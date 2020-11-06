**Example 1: Ending On-Cloud MixTranscoding**

This example shows you how to end On-Cloud MixTranscoding for the room whose ID is 3560.

Input: 

```
tccli trtc StopMCUMixTranscode --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RoomId 3560
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

