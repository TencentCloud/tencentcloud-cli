**Example 1: 删除 EdgeKV 命名空间**

删除站点 zone-3j1xw7910arp 下的命名空间 ns-011。

Input: 

```
tccli teo DeleteEdgeKVNamespace --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --Namespace ns-011
```

Output: 
```
{
    "Response": {
        "RequestId": "537e3551-918f-4f6d-814d-540dc57e0216"
    }
}
```

