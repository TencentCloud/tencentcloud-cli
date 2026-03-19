**Example 1: 修改泳道组**



Input: 

```
tccli tse ModifyGovernanceLaneGroups --cli-unfold-argument  \
    --InstanceId abc \
    --LaneGroups.0.Name abc \
    --LaneGroups.0.ID abc \
    --LaneGroups.0.TrafficEntries.0.EntryType abc \
    --LaneGroups.0.TrafficEntries.0.TSEGatewaySelector.GatewayId abc \
    --LaneGroups.0.TrafficEntries.0.TSEGatewaySelector.Services abc \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Namespace abc \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Service abc \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Labels.0.Key abc \
    --LaneGroups.0.TrafficEntries.0.ServiceGatewaySelector.Labels.0.Value abc \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Namespace abc \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Service abc \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Labels.0.Key abc \
    --LaneGroups.0.TrafficEntries.0.ServiceSelector.Labels.0.Value abc \
    --LaneGroups.0.Destinations.0.Namespace abc \
    --LaneGroups.0.Destinations.0.Service abc \
    --LaneGroups.0.Destinations.0.Labels.0.LabelKey abc \
    --LaneGroups.0.Destinations.0.Labels.0.LabelValue abc \
    --LaneGroups.0.Destinations.0.Labels.0.LabelType abc \
    --LaneGroups.0.Destinations.0.Labels.0.LabelValueType abc \
    --LaneGroups.0.Description abc \
    --LaneGroups.0.Rules.0.ID abc \
    --LaneGroups.0.Rules.0.Name abc \
    --LaneGroups.0.Rules.0.LaneGroup abc \
    --LaneGroups.0.Rules.0.Enable True \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Type abc \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Key abc \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Value.Type abc \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Value.Value abc \
    --LaneGroups.0.Rules.0.TrafficLabels.0.Value.ValueType abc \
    --LaneGroups.0.Rules.0.TrafficMatchMode abc \
    --LaneGroups.0.Rules.0.LaneMatchMode abc \
    --LaneGroups.0.Rules.0.Description abc \
    --LaneGroups.0.Rules.0.LaneLabelValue abc \
    --LaneGroups.0.Rules.0.CreateTime abc \
    --LaneGroups.0.Rules.0.EnableTime abc \
    --LaneGroups.0.Rules.0.ModifyTime abc \
    --LaneGroups.0.Rules.0.Priority 0 \
    --LaneGroups.0.Rules.0.Revision abc \
    --LaneGroups.0.Revision abc \
    --LaneGroups.0.CreateTime abc \
    --LaneGroups.0.ModifyTime abc \
    --LaneGroups.0.Consistency abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

