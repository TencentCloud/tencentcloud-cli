**Example 1: LinkNamespaceList**



Input: 

```
tccli tcm LinkNamespaceList --cli-unfold-argument  \
    --MeshId abc \
    --Cluster.ClusterId abc \
    --Cluster.DisplayName abc \
    --Cluster.Region abc \
    --Cluster.Role abc \
    --Cluster.VpcId abc \
    --Cluster.SubnetId abc \
    --Cluster.State abc \
    --Cluster.LinkedTime 2020-09-22T00:00:00+00:00 \
    --Cluster.Config.AutoInjectionNamespaceList abc \
    --Cluster.Config.IngressGatewayList.0.Name abc \
    --Cluster.Config.IngressGatewayList.0.Namespace abc \
    --Cluster.Config.IngressGatewayList.0.ClusterId abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.LoadBalancerType abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.SubnetId abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.InternetChargeType abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.InternetMaxBandwidthOut 0 \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ZoneID abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.VipIsp abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.TgwGroupName abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.AddressIPVersion abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.Tags.0.Key abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.Tags.0.Value abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.Tags.0.Passthrough True \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L4Clusters.0.ClusterId abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L4Clusters.0.Zone abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L7Clusters.0.ClusterId abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L7Clusters.0.Zone abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.CrossRegionConfig.CrossRegionID abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.CrossRegionConfig.CrossType abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.CrossRegionConfig.CrossVpcID abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.MasterZoneID abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.SlaveZoneID abc \
    --Cluster.Config.IngressGatewayList.0.Service.Type abc \
    --Cluster.Config.IngressGatewayList.0.Service.CLBDirectAccess True \
    --Cluster.Config.IngressGatewayList.0.Service.ExternalTrafficPolicy abc \
    --Cluster.Config.IngressGatewayList.0.Workload.Replicas 0 \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Limits.0.Name abc \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Limits.0.Quantity abc \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Requests.0.Name abc \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Requests.0.Quantity abc \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.MinReplicas 0 \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.MaxReplicas 0 \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Type abc \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName abc \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue abc \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.Name abc \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageUtilization 0 \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageValue abc \
    --Cluster.Config.IngressGatewayList.0.Workload.SelectedNodeList abc \
    --Cluster.Config.IngressGatewayList.0.Workload.DeployMode abc \
    --Cluster.Config.IngressGatewayList.0.Status.LoadBalancer.LoadBalancerId abc \
    --Cluster.Config.IngressGatewayList.0.Status.LoadBalancer.LoadBalancerName abc \
    --Cluster.Config.IngressGatewayList.0.Status.LoadBalancer.LoadBalancerVip abc \
    --Cluster.Config.IngressGatewayList.0.Status.LoadBalancer.LoadBalancerHostname abc \
    --Cluster.Config.IngressGatewayList.0.Status.CurrentVersion abc \
    --Cluster.Config.IngressGatewayList.0.Status.DesiredVersion abc \
    --Cluster.Config.IngressGatewayList.0.Status.State abc \
    --Cluster.Config.IngressGatewayList.0.LoadBalancerId abc \
    --Cluster.Config.EgressGatewayList.0.Name abc \
    --Cluster.Config.EgressGatewayList.0.Namespace abc \
    --Cluster.Config.EgressGatewayList.0.Workload.Replicas 0 \
    --Cluster.Config.EgressGatewayList.0.Workload.Resources.Limits.0.Name abc \
    --Cluster.Config.EgressGatewayList.0.Workload.Resources.Limits.0.Quantity abc \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.MinReplicas 0 \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.MaxReplicas 0 \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Type abc \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName abc \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue abc \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.Name abc \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageUtilization 0 \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageValue abc \
    --Cluster.Config.EgressGatewayList.0.Workload.SelectedNodeList abc \
    --Cluster.Config.EgressGatewayList.0.Workload.DeployMode abc \
    --Cluster.Config.EgressGatewayList.0.Status.CurrentVersion abc \
    --Cluster.Config.EgressGatewayList.0.Status.DesiredVersion abc \
    --Cluster.Config.EgressGatewayList.0.Status.State abc \
    --Cluster.Config.Istiod.Workload.Replicas 0 \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.MinReplicas 0 \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.MaxReplicas 0 \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Type abc \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName abc \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue abc \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.Name abc \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageUtilization 0 \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageValue abc \
    --Cluster.Config.Istiod.Workload.SelectedNodeList abc \
    --Cluster.Config.Istiod.Workload.DeployMode abc \
    --Cluster.Config.DeployConfig.NodeSelectType abc \
    --Cluster.Config.DeployConfig.Nodes abc \
    --Cluster.Config.AutoInjectionNamespaceStateList.0.Namespace abc \
    --Cluster.Config.AutoInjectionNamespaceStateList.0.State abc \
    --Cluster.Status.LinkState abc \
    --Cluster.Status.LinkErrorDetail abc \
    --Cluster.Type abc \
    --Cluster.HostedNamespaces abc
```

Output: 
```
{
    "Response": {
        "NamespaceList": [
            {
                "Namespace": "abc",
                "Status": "abc",
                "Reason": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

