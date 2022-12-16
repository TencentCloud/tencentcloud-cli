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
        "RequestId": "c33a0bd5-f41a-4ac5-8480-e31fa972ec7e",
        "Result": true
    }
}
```

