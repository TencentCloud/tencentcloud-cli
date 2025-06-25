**Example 1: 查询实例支持代理版本和参数**



Input: 

```
tccli cdb DescribeProxySupportParam --cli-unfold-argument  \
    --InstanceId cdb-aykuksx3
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "ProxyVersion": "1.3.1",
        "SupportPool": true,
        "PoolMin": 1,
        "PoolMax": 10,
        "SupportTransSplit": true,
        "SupportTransSplitMinVersion": "1.3.1",
        "SupportPoolMinVersion": "1.1.1",
        "SupportReadOnly": true,
        "SupportAutoLoadBalance": true,
        "SupportAccessMode": true
    }
}
```

