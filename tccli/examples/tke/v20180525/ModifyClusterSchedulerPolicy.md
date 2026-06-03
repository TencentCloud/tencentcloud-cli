**Example 1: 修改调度器参数信息**



Input: 

```
tccli tke ModifyClusterSchedulerPolicy --cli-unfold-argument  \
    --ClusterId cls-ncmx45jw \
    --SchedulerPolicyConfig.0.SchedulerName default-scheduler \
    --SchedulerPolicyConfig.0.PluginConfigs.0.Name NodeResourcesFit \
    --SchedulerPolicyConfig.0.PluginConfigs.0.Args eyJraW5kIjoiTm9kZVJlc291cmNlc0ZpdEFyZ3MiLCJhcGlWZXJzaW9uIjoia3ViZXNjaGVkdWxlci5jb25maWcuazhzLmlvL3YxIiwic2NvcmluZ1N0cmF0ZWd5Ijp7InR5cGUiOiJMZWFzdEFsbG9jYXRlZCIsInJlc291cmNlcyI6W3sibmFtZSI6ImNwdSIsIndlaWdodCI6MX0seyJuYW1lIjoibWVtb3J5Iiwid2VpZ2h0IjoxfV19fQ== \
    --SchedulerPolicyConfig.0.PluginSet.Enabled.0.Name NodeResourcesFit \
    --SchedulerPolicyConfig.0.PluginSet.Enabled.0.Weight 1 \
    --SchedulerPolicyConfig.0.PluginSet.Disabled.0.Name DefaultPreemption \
    --SchedulerPolicyConfig.0.PluginSet.Disabled.0.Weight 0 \
    --Extenders.0.ExtenderClientConfig.Service.Name m-scheduler-extender \
    --Extenders.0.ExtenderClientConfig.Service.Namespace default \
    --Extenders.0.ExtenderClientConfig.Service.Path scheduler \
    --Extenders.0.ExtenderClientConfig.Service.Port 8010 \
    --Extenders.0.ExtenderClientConfig.Service.Scheme http \
    --Extenders.0.FilterVerb scheduler/test1 \
    --Extenders.0.PrioritizeVerb scheduler/score \
    --Extenders.0.Weight 1 \
    --ClientConnection.QPS 51 \
    --ClientConnection.Burst 101 \
    --HighPerformance True
```

Output: 
```
{
    "Response": {
        "RequestId": "96fbca81-f0fe-46d6-ad81-ab87f6ae24f6"
    }
}
```

