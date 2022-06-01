**Example 1: 创建边缘计算集群示例**



Input: 

```
tccli tke CreateTKEEdgeCluster --cli-unfold-argument  \
    --K8SVersion 1.12.4 \
    --VpcId vpc-xxx \
    --ClusterName for_test \
    --PodCIDR 172.16.0.0/20 \
    --ServiceCIDR 192.168.0.0/18
```

Output: 
```
{
    "Response": {
        "ClusterId": "cls-xxx",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

