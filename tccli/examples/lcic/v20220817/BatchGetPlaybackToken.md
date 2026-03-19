**Example 1: BatchGetPlaybackToken**



Input: 

```
tccli lcic BatchGetPlaybackToken --cli-unfold-argument  \
    --SdkAppId 3923193 \
    --RoomIds 305745891 \
    --ExpireSeconds 0
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "RoomId": 305745891,
                "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.***********p******A1NzQ1ODkxLCJleHAiOjQ5MjQyOTMzMzh9.WvaoCqfns************lRXNr6tgylgWmM1ocAz0kw"
            }
        ],
        "Total": 1,
        "RequestId": "9a4a9095-f250-4dcd-8650-21861a0ebbb0"
    }
}
```

