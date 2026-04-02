**Example 1: 创建泳道组**

创建泳道组

Input: 

```
tccli tse CreateGovernanceLaneGroups --cli-unfold-argument  \
    --InstanceId ins-17dhh123 \
    --LaneGroups.0.Name sct \
    --LaneGroups.0.ID db33e953bfd7467abe34f40f23ca1ada \
    --LaneGroups.0.TrafficEntries.0.EntryType polarismesh.cn/gateway/spring-cloud-gateway \
    --LaneGroups.0.TrafficEntries.0.TSEGatewaySelector.GatewayId 15d28168fe894299b50d49b35193867c \
    --LaneGroups.0.TrafficEntries.0.TSEGatewaySelector.Services blue \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Namespace default1 \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Service springcloudt \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Labels.0.Key color \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Labels.0.Value blue \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Namespace default1 \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Service springcloudt \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Labels.0.Key color \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Labels.0.Value blue \
    --LaneGroups.0.Destinations.0.Namespace polaris \
    --LaneGroups.0.Destinations.0.Service Polaris \
    --LaneGroups.0.Destinations.0.Labels.0.LabelKey color \
    --LaneGroups.0.Destinations.0.Labels.0.LabelValue blue \
    --LaneGroups.0.Destinations.0.Labels.0.LabelType HEADER \
    --LaneGroups.0.Destinations.0.Labels.0.LabelValueType TEXT \
    --LaneGroups.0.Description lanegroup \
    --LaneGroups.0.Rules.0.ID 15d28168fe8942sdd10d49b35193867c \
    --LaneGroups.0.Rules.0.Name polaris \
    --LaneGroups.0.Rules.0.LaneGroup polaris \
    --LaneGroups.0.Rules.0.Enable True \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Type HEADER \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Key color \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Value.Type HEADER \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Value.Value blue \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Value.ValueType TEXT \
    --LaneGroups.0.Rules.0.TrafficMatchMode sct \
    --LaneGroups.0.Rules.0.LaneMatchMode PERMISSIVE \
    --LaneGroups.0.Rules.0.Description lanegroup \
    --LaneGroups.0.Rules.0.LaneLabelValue blue \
    --LaneGroups.0.Rules.0.CreateTime 2026-01-15 11:43:21 \
    --LaneGroups.0.Rules.0.EnableTime 2026-01-15 11:43:21 \
    --LaneGroups.0.Rules.0.ModifyTime 2026-01-15 11:43:21 \
    --LaneGroups.0.Rules.0.Priority 0 \
    --LaneGroups.0.Rules.0.Revision a023fd6b2f1441158699177ad3a86213 \
    --LaneGroups.0.Revision a023fd6b2f1441158699177ad3a86213 \
    --LaneGroups.0.CreateTime 2026-01-15 11:43:21 \
    --LaneGroups.0.ModifyTime 2026-01-15 11:43:21 \
    --LaneGroups.0.Consistency LaneCallerService
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "15d28168fe894299b50d49b35193867c"
    }
}
```

