**Example 1: 创建集群**

创建集群

Input: 

```
tccli tsf CreateCluster --cli-unfold-argument  \
    --VpcId vpc-xxxxxxx \
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
        "Result": "abc",
        "RequestId": "abc"
    }
}
```

