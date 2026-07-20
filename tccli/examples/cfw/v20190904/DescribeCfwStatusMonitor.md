**Example 1: 发现场景和二级下拉选项**

describe_scene 用来发现可用 metric/perspective 组合、默认值、选择项要求和二级下拉 available_options；fetch_scene 应原样使用发现结果。输出为字段结构节选，数组仅展示代表值。

Input: 

```
tccli cfw DescribeCfwStatusMonitor --cli-unfold-argument  \
    --Op describe_scene \
    --FirewallType internet_edge
```

Output: 
```
{
    "Response": {
        "Data": "{\"op\":\"describe_scene\",\"scene\":{\"firewall_type\":\"internet_edge\",\"metric_options\":[\"bandwidth\"],\"perspective_options\":{\"bandwidth\":[\"ip\"]},\"default_metric\":\"bandwidth\",\"default_perspective\":{\"bandwidth\":\"ip\"},\"selection_required_by_metric\":{\"bandwidth\":false},\"selection_kind_by_metric\":{\"bandwidth\":\"region\"},\"time_preset_options\":[\"1h\",\"24h\",\"7d\"]},\"selection\":{\"available_options\":[{\"id\":\"__all__\",\"name\":\"全部地域\"},{\"id\":\"ap-guangzhou\",\"name\":\"广州\"}]}}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 2: 拉取互联网边界状态监控快照**

fetch_scene 拉取一个具体场景快照；它不是单纯 metrics 查询，还包含场景选择、概览和列表/明细视角。

Input: 

```
tccli cfw DescribeCfwStatusMonitor --cli-unfold-argument  \
    --Op fetch_scene \
    --FirewallType internet_edge \
    --Metric bandwidth \
    --Perspective ip \
    --SelectionId ap-guangzhou \
    --TimePreset 24h \
    --OverviewOnly True \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": "{\"op\":\"fetch_scene\",\"data\":{\"overview\":{\"InputMax\":1024}}}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

