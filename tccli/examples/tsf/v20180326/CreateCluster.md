**Example 1: 创建集群**

创建集群

Input: 

```
tccli tsf CreateCluster --cli-unfold-argument  \
    --VpcId vpc-6a79x94v \
    --ClusterName DEMO-DOCKER \
    --TsfZoneId 100004 \
    --ClusterType C \
    --ClusterCIDR 172.16.0.0/16 \
    --TsfRegionId ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Result": "cluster-6a79x94v",
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

