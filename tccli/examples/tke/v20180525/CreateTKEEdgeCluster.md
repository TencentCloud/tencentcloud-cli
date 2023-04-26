**Example 1: 创建边缘计算集群示例**

创建边缘计算集群

Input: 

```
tccli tke CreateTKEEdgeCluster --cli-unfold-argument  \
    --ClusterName for_test \
    --PodCIDR 172.16.0.0/20 \
    --VpcId vpc-xxx \
    --ServiceCIDR 192.168.0.0/18 \
    --K8SVersion 1.12.4
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

