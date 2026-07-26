**Example 1: 忽略新告警中心事件**

按 DescribeCfwAlerts 返回的事件 ID 忽略告警事件；存在 alerts[].current_event_id 时使用该值，否则使用 alerts[].event_id。HandleIdList 固定传 [""]。

Input: 

```
tccli cfw CreateAlertCenterOmit --cli-unfold-argument  \
    --HandleIdList  \
    --TableType AlertTable \
    --HandleEventIdList 00000000000000000000000000000001
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000001",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 2: 忽略告警日志**

按 DescribeLogs 返回的 log_id 忽略告警中心记录。

Input: 

```
tccli cfw CreateAlertCenterOmit --cli-unfold-argument  \
    --HandleIdList 00000000000000000000000000000002 \
    --TableType AlertTable
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000002",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

**Example 3: 忽略拦截记录**

按 DescribeBlockList 返回的 Data[].UniqueId 或 TopData[].UniqueId 忽略拦截记录。

Input: 

```
tccli cfw CreateAlertCenterOmit --cli-unfold-argument  \
    --HandleIdList 00000000000000000000000000000003 \
    --TableType InterceptionTable
```

Output: 
```
{
    "Response": {
        "RequestId": "00000000-0000-4000-8000-000000000003",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

