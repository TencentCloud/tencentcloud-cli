**Example 1: DescribePlaybackList**



Input: 

```
tccli lcic DescribePlaybackList --cli-unfold-argument  \
    --SdkAppId 3923193 \
    --Page 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": 1770625573,
                "Duration": 0,
                "PlaybackUrl": "https://****s.q***udcla**.com/pl******/***ex.html?classid=379125945&token=eyJhbGciOiJIUzI1NiIsIn*****6*******9.eyJjbGFzc19pZCI6Mzc5MTI1OTQ1LCJleHAiOjE3Nz***T**N*****H-0GlGD4YcD-INQP0UDixn0****jrzYTNZamjI7CDs",
                "RoomId": 379125945
            }
        ],
        "Total": 1,
        "RequestId": "9be3f8dd-31ed-4b13-896d-dddbc3b21ea3"
    }
}
```

