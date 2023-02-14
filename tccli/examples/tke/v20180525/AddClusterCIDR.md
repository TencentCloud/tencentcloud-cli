**Example 1: 给集群增加ClusterCIDR**



Input: 

```
tccli tke AddClusterCIDR --cli-unfold-argument  \
    --ClusterId cls-abcdefgh \
    --ClusterCIDRs 10.0.0.0/14 192.168.0.0/16 \
    --IgnoreClusterCIDRConflict True
```

Output: 
```
{
    "Response": {
        "RequestId": "defc0237-d413-4079-9faa-7f3ff928d224"
    }
}
```

