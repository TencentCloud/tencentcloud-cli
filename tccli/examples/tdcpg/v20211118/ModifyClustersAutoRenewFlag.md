**Example 1: 修改集群自动续费**



Input: 

```
tccli tdcpg ModifyClustersAutoRenewFlag --cli-unfold-argument  \
    --ClusterIdSet tdcpg-xxx \
    --AutoRenewFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

