**Example 1: 销毁容器EMR-TKE集群DynamicInstance**



Input: 

```
tccli emr TerminateDynamicInstances --cli-unfold-argument  \
    --InstanceId emr-34u4s2qh \
    --DynamicInstanceType RayCluster \
    --DynamicInstanceIds 30
```

Output: 
```
{
    "Response": {
        "RequestId": "ee5ad5b3-3f3e-41ca-b7a2-1546b29f4611",
        "FlowId": 213
    }
}
```

