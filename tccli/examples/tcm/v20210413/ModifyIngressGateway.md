**Example 1: ModifyIngressGateway**



Input: 

```
tccli tcm ModifyIngressGateway --cli-unfold-argument  \
    --Workload.SelectedNodeList xx \
    --Workload.HorizontalPodAutoscaler.MinReplicas 0 \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue xx \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName xx \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Type xx \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageUtilization 0 \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Resource.Name xx \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Resource.TargetAverageValue xx \
    --Workload.HorizontalPodAutoscaler.MaxReplicas 0 \
    --Workload.Resources.Requests.0.Name xx \
    --Workload.Resources.Requests.0.Quantity xx \
    --Workload.Resources.Limits.0.Name xx \
    --Workload.Resources.Limits.0.Quantity xx \
    --Workload.Replicas 0 \
    --Service.ExternalTrafficPolicy xx \
    --Service.Type xx \
    --Service.CLBDirectAccess True \
    --MeshId xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

