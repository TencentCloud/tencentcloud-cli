**Example 1: CreateIngressGateway**



Input: 

```
tccli tcm CreateIngressGateway --cli-unfold-argument  \
    --Workload.SelectedNodeList 10.0.0.2 \
    --Workload.HorizontalPodAutoscaler.MinReplicas 1 \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Pods.TargetAverageValue 80 \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Pods.MetricName k8s_pod_rate_cpu_core_used_request \
    --Workload.HorizontalPodAutoscaler.Metrics.0.Type Pods \
    --Workload.HorizontalPodAutoscaler.MaxReplicas 3 \
    --Workload.Resources.Requests.0.Name cpu \
    --Workload.Resources.Requests.0.Quantity 1 \
    --Workload.Resources.Limits.0.Name cpu \
    --Workload.Resources.Limits.0.Quantity 2 \
    --Workload.Replicas 1 \
    --Name istio-ingressgateway \
    --Service.ExternalTrafficPolicy Cluster \
    --Service.Type LoadBalancer \
    --Service.CLBDirectAccess True \
    --ClusterId cls-xxxxxxxx \
    --Namespace istio-system \
    --MeshId mesh-xxxxxxxx \
    --LoadBalancer.LoadBalancerType OPEN
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

