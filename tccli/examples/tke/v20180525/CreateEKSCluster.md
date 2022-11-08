**Example 1: 创建弹性集群示例**

创建托管集群

Input: 

```
tccli tke CreateEKSCluster --cli-unfold-argument  \
    --ServiceSubnetId subnet-xxxx \
    --VpcId vpc-xxx \
    --K8SVersion 1.12.4 \
    --ClusterName for_test \
    --SubnetIds subnet-xxxx \
    --DnsServers.0.Domain exam.com \
    --DnsServers.0.DnsServers 10.2.2.88:53 \
    --ClusterDesc my_test_cluster
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

