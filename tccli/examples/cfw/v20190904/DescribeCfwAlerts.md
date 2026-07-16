**Example 1: 查询高危阻断告警**

按告警级别和处置状态过滤；Response.Data 中 total 是聚合告警事件数，occurrence_count 是单个聚合告警事件的告警发生次数/命中次数。

Input: 

```
tccli cfw DescribeCfwAlerts --cli-unfold-argument  \
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

