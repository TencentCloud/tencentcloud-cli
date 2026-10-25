**Example 1: 查询拨测维度分布**

按指定维度拆分拨测次数、时延和丢包率。

Input: 

```
tccli rum DescribeTDEMDialDimensions --cli-unfold-argument  \
    --AppId 5 \
    --StartTime 1789026600000 \
    --EndTime 1791618600000 \
    --Dimension country \
    --TaskId 16 \
    --Platform android \
    --AppVersion 1.0.0 \
    --Device sdk_gphone64_arm64 \
    --NetType wifi \
    --Operator 电信 \
    --ClientRegion 广东 \
    --TargetIp 183.2.172.177
```

Output: 
```
{
    "Response": {
        "Dimension": "country",
        "Items": [
            {
                "Value": "中国",
                "ExecutionCount": 1571,
                "SuccessCount": 1275,
                "FailCount": 296,
                "AvgDuration": 260.36431372549015,
                "AvgLoss": 0
            }
        ],
        "RequestId": "27fca02a-cbe6-4c4d-b13b-4cbc14c3ca4b"
    }
}
```

