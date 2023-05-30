**Example 1: 给资源包绑定集群**

给资源包绑定集群

Input: 

```
tccli cynosdb ModifyResourcePackageClusters --cli-unfold-argument  \
    --PackageId abc \
    --BindClusterIds abc \
    --UnbindClusterIds abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

