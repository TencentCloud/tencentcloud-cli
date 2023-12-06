**Example 1: 检查集群的CIDR是否冲突**



Input: 

```
tccli tke CheckClusterCIDR --cli-unfold-argument  \
    --VpcId vpc-xxxxxx \
    --ClusterCIDR “192.168.0.0/16”
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459398",
        "ConflictType": "",
        "ConflictMsg": "",
        "IsConflict": false
    }
}
```

