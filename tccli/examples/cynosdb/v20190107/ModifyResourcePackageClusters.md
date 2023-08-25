**Example 1: 给资源包绑定集群**

给资源包绑定集群

Input: 

```
tccli cynosdb ModifyResourcePackageClusters --cli-unfold-argument  \
    --PackageId package-abcd1234 \
    --BindClusterIds cynosdbmysql-1234abcd \
    --UnbindClusterIds cynosdbmysql-1122aabb
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

