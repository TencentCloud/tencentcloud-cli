**Example 1: 查询已导入的 TKE 集群详情**

根据 EmrClusterId 查询已导入的 TKE 集群详情，附带 CLB / Prometheus / CLS 名称

Input: 

```
tccli dlc DescribeTkeClusterImportInfo --cli-unfold-argument  \
    --EmrClusterId emr-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "PartitionName": "my-emr-tke-partition",
        "EmrClusterId": "emr-xxxxxxxx",
        "CosBucketId": "my-bucket-1250000000",
        "PrometheusInstanceId": "prom-xxxxxxxx",
        "PrometheusInstanceName": "my-prom-instance",
        "LoadBalancerId": "lb-xxxxxxxx",
        "LoadBalancerName": "my-clb",
        "ContainerLogTopicId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "ContainerLogTopicName": "container-logs",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

