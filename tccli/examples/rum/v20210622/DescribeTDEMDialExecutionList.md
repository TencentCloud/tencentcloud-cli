**Example 1: 查询拨测执行记录**

按时间窗分页查询拨测批次，一批次对应一行。

Input: 

```
tccli rum DescribeTDEMDialExecutionList --cli-unfold-argument  \
    --AppId 5 \
    --StartTime 1788852300000 \
    --EndTime 1791444300000 \
    --TaskId 9 \
    --Platform android \
    --AppVersion 1.0.0 \
    --Device sdk_gphone64_arm64 \
    --NetType wifi \
    --Operator 电信 \
    --ClientRegion 广东 \
    --TargetIp 183.2.172.177 \
    --Limit 20 \
    --Offset 0 \
    --Success True
```

Output: 
```
{
    "Response": {
        "TotalCount": 516,
        "ExecutionSet": [
            {
                "TaskId": "9",
                "TaskName": "android-audience-user",
                "TaskSessionId": "6b37f3fe-0b2c-43c5-8bc1-a8cad1a60202",
                "StartTime": 1791444282154,
                "Platform": "android",
                "AppVersion": "1.0.0",
                "Device": "sdk_gphone64_arm64",
                "NetType": "",
                "Operator": "电信",
                "Region": "广东",
                "TargetIps": [
                    "183.2.172.177"
                ],
                "TargetIpGeo": [
                    {
                        "Ip": "183.2.172.177",
                        "Region": "广东",
                        "Operator": "电信"
                    }
                ],
                "Success": true,
                "AvgDuration": 132.1,
                "HasMTR": false,
                "SessionId": "bbd4851f-d07b-4de0-ad5a-3d04f68e3f84"
            }
        ],
        "RequestId": "4e67667d-7540-4efb-956c-28dcc82b58f1"
    }
}
```

