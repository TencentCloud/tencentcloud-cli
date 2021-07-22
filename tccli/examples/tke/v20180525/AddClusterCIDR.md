**Example 1: 给集群增加ClusterCIDR**



Input: 

```
tccli tke AddClusterCIDR --cli-unfold-argument  \
    --ClusterId xx \
    --ClusterCIDRs 10.0.0.0/14 192.168.0.0/16 \
    --IgnoreClusterCIDRConflict True
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

