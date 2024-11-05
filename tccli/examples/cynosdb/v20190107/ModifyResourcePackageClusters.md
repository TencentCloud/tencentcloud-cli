**Example 1: 给资源包绑定集群**

给资源包绑定集群

Input: 

```
tccli cynosdb ModifyResourcePackageClusters --cli-unfold-argument  \
    --PackageId package-3crr5ldh \
    --BindClusterIds cynosdbmysql-mwg7121t \
    --UnbindClusterIds cynosdbmysql-kueh122w
```

Output: 
```
{
    "Response": {
        "RequestId": "a5706353-296a-4992-ad07-ac4a48eeba43"
    }
}
```

