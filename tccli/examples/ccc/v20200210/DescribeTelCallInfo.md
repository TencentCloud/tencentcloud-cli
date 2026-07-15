**Example 1: 获取电话呼叫统计信息示例**

获取电话呼叫统计信息

Input: 

```
tccli ccc DescribeTelCallInfo --cli-unfold-argument  \
    --StartTimeStamp 1773041460 \
    --EndTimeStamp 1773042460 \
    --SdkAppIdList 140000000
```

Output: 
```
{
    "Response": {
        "TelCallOutCount": 0,
        "TelCallInCount": 0,
        "SeatUsedCount": 0,
        "VOIPCallInCount": 0,
        "AsrOfflineCount": 0,
        "AsrRealtimeCount": 0,
        "RequestId": "sfahfj-fasf"
    }
}
```

