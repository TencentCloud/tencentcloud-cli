**Example 1: 创建应用实例**

创建应用实例

Input: 

```
tccli camp CreateInstance --cli-unfold-argument  \
    --ProjectID abc \
    --ApplicationID abc \
    --EnvironmentName abc \
    --Name testinstance \
    --Components.0.Name abc \
    --Components.0.Type abc \
    --Components.0.Properties.K8sObjects abc \
    --Components.0.Properties.StatefulSetPlus abc \
    --Components.0.Properties.StatefulSet abc \
    --Components.0.Properties.Deployment abc \
    --Components.0.Properties.TAPP abc \
    --Components.0.Traits.0.Name abc \
    --Components.0.Traits.0.Type abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.Type abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.MaxUnavailable abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.MaxSurge abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.InPlaceUpdateFlag True \
    --Components.0.Traits.0.Properties.UpdateStrategy.AutoBatchUpdate.MaxFailed abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.AutoBatchUpdate.Details.0.ClusterLabelSelector.0.Key abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.AutoBatchUpdate.Details.0.ClusterLabelSelector.0.Value abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.AutoBatchUpdate.Details.0.PodNumToUpdate abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.AutoBatchUpdate.Details.0.BatchInterval 1 \
    --Components.0.Traits.0.Properties.UpdateStrategy.RollingUpdate.Clusters abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.RollingUpdate.ClusterLabelSelectors.0.MatchLabels.0.Key abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.RollingUpdate.ClusterLabelSelectors.0.MatchLabels.0.Value abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.RollingUpdate.ClusterLabelSelectors.0.ReleaseOrder 1 \
    --Components.0.Traits.0.Properties.UpdateStrategy.RollingUpdate.Partition 0 \
    --Components.0.Traits.0.Properties.UpdateStrategy.BatchUpdate.MaxFailed abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.BatchUpdate.PodsToUpdate abc \
    --Components.0.Traits.0.Properties.UpdateStrategy.Pause True \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.Name abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.PolarisNamespace abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.PolarisName abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.Token abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.Weight 0 \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.Ports.0.Name abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.Ports.0.Port 0 \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.Ports.0.Protocol abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.SyncMode abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.SiteZone abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.TTL 0 \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.InstanceLabel.0.Key abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.InstanceLabel.0.Value abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.CustomWeight.0.ClusterID abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.CustomWeight.0.PodName abc \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.CustomWeight.0.Weight 0 \
    --Components.0.Traits.0.Properties.Polaris.Objects.0.CustomWeight.0.Port 1 \
    --Components.0.Traits.0.Properties.Replicas.Replicas 0 \
    --Components.0.Traits.0.Properties.HPA.MinReplicas 0 \
    --Components.0.Traits.0.Properties.HPA.MaxReplicas 0 \
    --Components.0.Traits.0.Properties.HPA.Tolerance 0 \
    --Components.0.Traits.0.Properties.HPA.ReSyncPeriod 0 \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleUp.StabilizationWindowSeconds 0 \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleUp.SelectPolicy abc \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleUp.Policies.0.Type abc \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleUp.Policies.0.Value 0 \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleUp.Policies.0.PeriodSeconds 0 \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleDown.StabilizationWindowSeconds 0 \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleDown.SelectPolicy abc \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleDown.Policies.0.Type abc \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleDown.Policies.0.Value 0 \
    --Components.0.Traits.0.Properties.HPA.Behavior.ScaleDown.Policies.0.PeriodSeconds 0 \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Type abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.Target.Type abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.Target.Value abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.Target.AverageValue abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.Target.AverageUtilization 0 \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.Metric.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.Container abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.DescribedObject.Kind abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.DescribedObject.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Object.DescribedObject.APIVersion abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.Target.Type abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.Target.Value abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.Target.AverageValue abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.Target.AverageUtilization 0 \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.Metric.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.Container abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.DescribedObject.Kind abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.DescribedObject.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Pods.DescribedObject.APIVersion abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.Target.Type abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.Target.Value abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.Target.AverageValue abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.Target.AverageUtilization 0 \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.Metric.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.Container abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.DescribedObject.Kind abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.DescribedObject.Name abc \
    --Components.0.Traits.0.Properties.HPA.Metrics.0.Resource.DescribedObject.APIVersion abc \
    --Components.0.Traits.0.Properties.HPA.OverloadScale True \
    --Components.0.Traits.0.Properties.ZhiyanLog.Objects.0.Name abc \
    --Components.0.Traits.0.Properties.ZhiyanLog.Objects.0.Topic abc \
    --Components.0.Traits.0.Properties.ZhiyanLog.Objects.0.Type abc \
    --Components.0.Traits.0.Properties.ZhiyanLog.Objects.0.Container abc \
    --Components.0.Traits.0.Properties.ZhiyanLog.Objects.0.Config.Stream abc \
    --Components.0.Traits.0.Properties.ZhiyanLog.Objects.0.Config.Volume abc \
    --Components.0.Traits.0.Properties.ZhiyanLog.Objects.0.Config.Paths abc \
    --Policies.0.Name abc \
    --Policies.0.Type abc \
    --Policies.0.Properties.Placement.Type abc \
    --Policies.0.Properties.Placement.Region abc \
    --Policies.0.Properties.Placement.Zones.0.Zone abc \
    --Policies.0.Properties.Placement.Zones.0.Weight 0 \
    --Policies.0.Properties.Placement.Components abc \
    --Policies.0.Properties.Placement.Strategy abc \
    --Creator.Tencent.Name abc \
    --Source camp \
    --SourceURL http://127.0.0.1 \
    --ReadOnly True
```

Output: 
```
{
    "Response": {
        "InstanceID": "abc",
        "RequestId": "23641907-9449-4a5b-85d8-e1930762d126"
    }
}
```

