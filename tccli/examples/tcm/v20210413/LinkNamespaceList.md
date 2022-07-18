**Example 1: LinkNamespaceList**



Input: 

```
tccli tcm LinkNamespaceList --cli-unfold-argument  \
    --Cluster.Status.LinkErrorDetail xx \
    --Cluster.Status.LinkState xx \
    --Cluster.LinkedTime 2020-09-22T00:00:00+00:00 \
    --Cluster.VpcId xx \
    --Cluster.DisplayName xx \
    --Cluster.Type xx \
    --Cluster.Region xx \
    --Cluster.ClusterId xx \
    --Cluster.HostedNamespaces default alpha beta test6 \
    --Cluster.State xx \
    --Cluster.Role xx \
    --Cluster.SubnetId xx \
    --Cluster.Config.AutoInjectionNamespaceList xx \
    --Cluster.Config.DeployConfig.NodeSelectType xx \
    --Cluster.Config.DeployConfig.Nodes xx \
    --Cluster.Config.IngressGatewayList.0.Status.LoadBalancer.LoadBalancerName xx \
    --Cluster.Config.IngressGatewayList.0.Status.LoadBalancer.LoadBalancerVip xx \
    --Cluster.Config.IngressGatewayList.0.Status.LoadBalancer.LoadBalancerId xx \
    --Cluster.Config.IngressGatewayList.0.Workload.SelectedNodeList xx \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.MinReplicas 0 \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue xx \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName xx \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Type xx \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageUtilization 0 \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.Name xx \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageValue xx \
    --Cluster.Config.IngressGatewayList.0.Workload.HorizontalPodAutoscaler.MaxReplicas 0 \
    --Cluster.Config.IngressGatewayList.0.Workload.DeployMode xx \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Requests.0.Name xx \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Requests.0.Quantity xx \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Limits.0.Name xx \
    --Cluster.Config.IngressGatewayList.0.Workload.Resources.Limits.0.Quantity xx \
    --Cluster.Config.IngressGatewayList.0.Workload.Replicas 0 \
    --Cluster.Config.IngressGatewayList.0.Name xx \
    --Cluster.Config.IngressGatewayList.0.Service.ExternalTrafficPolicy xx \
    --Cluster.Config.IngressGatewayList.0.Service.Type xx \
    --Cluster.Config.IngressGatewayList.0.Service.CLBDirectAccess True \
    --Cluster.Config.IngressGatewayList.0.Namespace xx \
    --Cluster.Config.IngressGatewayList.0.ClusterId xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancerId xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.VipIsp xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.Tags.0.Passthrough True \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.Tags.0.Value xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.Tags.0.Key xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L7Clusters.0.ClusterId xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L7Clusters.0.Zone xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L4Clusters.0.ClusterId xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ExtensiveClusters.L4Clusters.0.Zone xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.TgwGroupName xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.ZoneID xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.InternetMaxBandwidthOut 0 \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.LoadBalancerType xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.AddressIPVersion xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.SubnetId xx \
    --Cluster.Config.IngressGatewayList.0.LoadBalancer.InternetChargeType xx \
    --Cluster.Config.AutoInjectionNamespaceStateList.0.State xx \
    --Cluster.Config.AutoInjectionNamespaceStateList.0.Namespace xx \
    --Cluster.Config.EgressGatewayList.0.Workload.SelectedNodeList xx \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.MinReplicas 0 \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue xx \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName xx \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Type xx \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageUtilization 0 \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.Name xx \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageValue xx \
    --Cluster.Config.EgressGatewayList.0.Workload.HorizontalPodAutoscaler.MaxReplicas 0 \
    --Cluster.Config.EgressGatewayList.0.Workload.DeployMode xx \
    --Cluster.Config.EgressGatewayList.0.Workload.Resources.Requests.0.Name xx \
    --Cluster.Config.EgressGatewayList.0.Workload.Resources.Requests.0.Quantity xx \
    --Cluster.Config.EgressGatewayList.0.Workload.Replicas 0 \
    --Cluster.Config.EgressGatewayList.0.Namespace xx \
    --Cluster.Config.EgressGatewayList.0.Name xx \
    --Cluster.Config.Istiod.Workload.SelectedNodeList xx \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.MinReplicas 0 \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue xx \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName xx \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Type xx \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageUtilization 0 \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.Name xx \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageValue xx \
    --Cluster.Config.Istiod.Workload.HorizontalPodAutoscaler.MaxReplicas 0 \
    --Cluster.Config.Istiod.Workload.DeployMode xx \
    --Cluster.Config.Istiod.Workload.Replicas 0 \
    --MeshId xx
```

Output: 
```
{
    "Response": {
        "NamespaceList": [
            {
                "Status": "xx",
                "Reason": "xx",
                "Namespace": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

