**Example 1: 组测集群到云上**



Input: 

```
tccli monitor CreateExternalCluster --cli-unfold-argument  \
    --ClusterName test-cluster \
    --InstanceId prom-abcd \
    --ClusterRegion ap-shanghai
```

Output: 
```
{
    "Response": {
        "ClusterId": "ecls-abc",
        "RequestId": "abcd-abcd"
    }
}
```

