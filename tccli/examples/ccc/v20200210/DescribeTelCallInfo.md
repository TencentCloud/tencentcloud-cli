**Example 1: 获取电话呼叫统计信息示例**



Input: 

```
tccli ccc DescribeTelCallInfo --cli-unfold-argument  \
    --StartTimeStamp 0 \
    --EndTimeStamp 0 \
    --SdkAppIdList 0
```

Output: 
```
{
    "Response": {
        "RequestId": "53bccf04-0870-4520-8614-f4bdddfd68df",
        "TelCallOutCount": 10,
        "TelCallInCount": 10,
        "VoipCallInCount": 10,
        "SeatUsedCount": 50
    }
}
```

