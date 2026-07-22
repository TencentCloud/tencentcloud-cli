**Example 1: 忽略新告警中心事件**

按告警聚合事件 ID 忽略对应的告警日志；HandleIdList 中的空字符串用于满足公共请求结构的必填字段，并会在目标合并时被删除。

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

