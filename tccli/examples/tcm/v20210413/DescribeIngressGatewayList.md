**Example 1: DescribeIngressGatewayList**



Input: 

```
tccli tcm DescribeIngressGatewayList --cli-unfold-argument  \
    --MeshId mesh-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "IngressGatewayList": [
            {
                "Status": {
                    "LoadBalancer": {
                        "LoadBalancerName": "cls-xxxxxxxx_istio_istio-ingressgateway",
                        "LoadBalancerVip": "150.158.238.54",
                        "LoadBalancerId": "lb-xxxxxxxx"
                    }
                },
                "Workload": {
                    "SelectedNodeList": [
                        "10.0.0.2"
                    ],
                    "HorizontalPodAutoscaler": {
                        "MinReplicas": 1,
                        "Metrics": [
                            {
                                "Pods": {
                                    "TargetAverageValue": "80",
                                    "MetricName": "k8s_pod_rate_cpu_core_used_request"
                                },
                                "Type": "Pods"
                            }
                        ],
                        "MaxReplicas": 3
                    },
                    "Resources": {
                        "Requests": [
                            {
                                "Name": "cpu",
                                "Quantity": "1"
                            }
                        ],
                        "Limits": [
                            {
                                "Name": "cpu",
                                "Quantity": "2"
                            }
                        ]
                    },
                    "Replicas": 1
                },
                "Name": "istio-ingressgateway",
                "Service": {
                    "ExternalTrafficPolicy": "Cluster",
                    "Type": "LoadBalancer",
                    "CLBDirectAccess": true
                },
                "ClusterId": "cls-xxxxxxxx",
                "Namespace": "istio-system",
                "LoadBalancer": {
                    "LoadBalancerType": "OPEN"
                }
            }
        ]
    }
}
```

