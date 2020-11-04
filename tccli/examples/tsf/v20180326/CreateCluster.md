**Example 1: 创建集群**



Input: 

```
tccli tsf CreateCluster --cli-unfold-argument  \
    --ClusterName DEMO-DOCKER\
    --TsfRegionId ap-guangzhou\
    --TsfZoneId 100004\
    --ClusterType C\
    --VpcId vpc-xxxxxxx\
    --ClusterCIDR 172.16.0.0/16
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

