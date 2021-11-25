**Example 1: 缩容独立集群master节点**



Input: 

```
tccli tke ScaleInClusterMaster --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx \
    --ScaleInMasters.0.InstanceId ins-xxxxxxxx \
    --ScaleInMasters.0.NodeRole MASTER_ETCD \
    --ScaleInMasters.0.InstanceDeleteMode retain
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

