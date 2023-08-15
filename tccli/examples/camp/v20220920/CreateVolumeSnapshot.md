**Example 1: 创建卷快照**



Input: 

```
tccli camp CreateVolumeSnapshot --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ClusterID cls-mg7ol3cm \
    --Name fox-snap-3 \
    --PersistentVolumeClaimName ngx2-test-ngx2-0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

