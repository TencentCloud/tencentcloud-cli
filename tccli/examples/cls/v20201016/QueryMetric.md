**Example 1: 查询指标最新值**



Input: 

```
tccli cls QueryMetric --cli-unfold-argument  \
    --TopicId 8e7c3bd9-xxxx-xxxx-xxxx-207971e1f80f \
    --Query access_evaluation_duration_bucket \
    --Time 1695197431
```

Output: 
```
{
    "Response": {
        "RequestId": "1ee38aa1-xxxx-xxxx-xxxx-b1961a464c99",
        "ResultType": "vector",
        "Result": "[{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"0.00064\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"0.01024\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"0.04096\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"0.65536\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"2.62144\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"0.00016\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5805\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"+Inf\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"0.00256\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"0.16384\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5808\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"1e-05\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5593\"]},{\"metric\":{\"__name__\":\"access_evaluation_duration_bucket\",\"container\":\"grafana\",\"endpoint\":\"http\",\"instance\":\"172.17.0.6:3000\",\"job\":\"grafana\",\"le\":\"4e-05\",\"namespace\":\"monitoring\",\"pod\":\"grafana-6676ccf9c9-zjk62\",\"prometheus\":\"monitoring/k8s\",\"prometheus_replica\":\"prometheus-k8s-0\",\"service\":\"grafana\"},\"value\":[1695197431,\"5787\"]}]"
    }
}
```

