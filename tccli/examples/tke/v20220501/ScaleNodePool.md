**Example 1: 设置 TKE 节点池期望节点数**



Input: 

```
tccli tke ScaleNodePool --cli-unfold-argument  \
    --Replicas 10 \
    --ClusterId cls-ht45hcgx \
    --NodePoolId np-2xrt4w7h
```

Output: 
```
{
    "Response": {
        "RequestId": "b398fbff-f9db-40a3-8cbe-22b88aa7c8ca"
    }
}
```

