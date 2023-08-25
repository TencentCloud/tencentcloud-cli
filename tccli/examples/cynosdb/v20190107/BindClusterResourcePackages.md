**Example 1: 为集群绑定资源包**

为集群绑定资源包

Input: 

```
tccli cynosdb BindClusterResourcePackages --cli-unfold-argument  \
    --PackageIds 'package- abcd1234' \
    --ClusterId cynosdbmysql-1234abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "123456789-123456-123456789"
    }
}
```

