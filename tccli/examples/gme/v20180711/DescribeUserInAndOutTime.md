**Example 1: 拉取用户在房间得进出时间**

拉取用户在房间得进出时间

Input: 

```
tccli gme DescribeUserInAndOutTime --cli-unfold-argument  \
    --BizId 1400440313 \
    --RoomId 12675079 \
    --UserId 112675079
```

Output: 
```
{
    "Response": {
        "InOutList": [
            {
                "StartTime": 1606355700701,
                "EndTime": 1606355712545
            },
            {
                "StartTime": 1606355835221,
                "EndTime": 1606355983240
            },
            {
                "StartTime": 1606356131997,
                "EndTime": 1606356139161
            },
            {
                "StartTime": 1606356140241,
                "EndTime": 1606357417975
            },
            {
                "StartTime": 1606357498484,
                "EndTime": 1606357504722
            },
            {
                "StartTime": 1606357505783,
                "EndTime": 1606358646084
            },
            {
                "StartTime": 1606358708098,
                "EndTime": 1606358732251
            }
        ],
        "Duration": 2615453,
        "RequestId": "e6579213-8adf-4047-9b59-bfd3d0c0bb24"
    }
}
```

