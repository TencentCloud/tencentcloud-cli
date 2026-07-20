**Example 1: 按时间和命中次数查询告警**

StartTime 和 EndTime 限定查询窗口；Count 按 occurrence_count 排序；下一页把 Offset 增加本页 returned。

Input: 

```
tccli cfw DescribeCfwAlerts --cli-unfold-argument  \
    --StartTime 2026-06-01 00:00:00 \
    --EndTime 2026-06-02 00:00:00 \
    --OrderBy Count \
    --Order desc \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": "{\"total\":376,\"returned\":10,\"offset\":0,\"order_by\":\"Count\",\"order\":\"desc\",\"alerts\":[{\"event_id\":\"evt-1\",\"occurrence_count\":138}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 2: 查询高危阻断告警**

按告警级别和处置状态过滤；Response.Data 中 total 是聚合告警事件数，occurrence_count 是单个聚合告警事件的告警发生次数/命中次数。

Input: 

```
tccli cfw DescribeCfwAlerts --cli-unfold-argument  \
    --Level high \
    --ActionStatus blocked \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": "{\"total\":376,\"alerts\":[{\"event_id\":\"evt-1\",\"occurrence_count\":138}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

