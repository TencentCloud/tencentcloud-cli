**Example 1: 为集群绑定资源包**

为集群绑定资源包

Input: 

```
tccli cynosdb BindClusterResourcePackages --cli-unfold-argument  \
    --PackageIds abc \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

