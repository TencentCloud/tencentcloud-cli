**Example 1: 检查边缘计算集群的CIDR是否冲突示例**



Input: 

```
tccli tke CheckEdgeClusterCIDR --cli-unfold-argument  \
    --VpcId vpc-xxx \
    --PodCIDR 10.0.1.10/24 \
    --ServiceCIDR 192.168.0.0/16
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "ConflictCode": "0",
        "ConflictMsg": "OK"
    }
}
```

