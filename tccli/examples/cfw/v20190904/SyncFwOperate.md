**Example 1: 同步防火墙操作**

同步防火墙操作，包括同步防火墙路由（若vpc，专线网关等增加了Cidr，需要手动同步一下路由使之在防火墙上生效）等

Input: 

```
tccli cfw SyncFwOperate --cli-unfold-argument  \
    --SyncType abc \
    --FwType abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

