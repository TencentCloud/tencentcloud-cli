**Example 1: 导入 EMR-TKE 集群**

导入 EMR-TKE 集群并返回资源池 ID 与工作流 ID

Input: 

```
tccli dlc ImportTkeCluster --cli-unfold-argument  \
    --PartitionName my-emr-tke-pool \
    --EmrClusterId emr-xxxxxxxx \
    --CosBucketId my-bucket-1250000000 \
    --PrometheusInstanceId prom-xxxxxxxx \
    --LoadBalancerId lb-xxxxxxxx \
    --ContainerLogTopicId xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
    --NodeLabels.0.Key ray-nexus/pool \
    --NodeLabels.0.Value default \
    --NodeLabels.1.Key kubernetes.io/os \
    --NodeLabels.1.Value linux \
    --PartitionDescription default partition for EMR-TKE pool
```

Output: 
```
{
    "Response": {
        "ResourcePoolId": 1001,
        "ResourcePoolCode": "rp-abcdefgh",
        "WorkflowId": 200001,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

