**Example 1: 创建 EdgeKV 命名空间**

在站点 zone-3j1xw7910arp 下创建一个名为 ns-011 的 EdgeKV 命名空间，描述为 remark。

Input: 

```
tccli teo CreateEdgeKVNamespace --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --Namespace ns-011 \
    --Remark remark
```

Output: 
```
{
    "Response": {
        "RequestId": "6204eccd-8da9-4b9c-b52c-0c28b5563a87"
    }
}
```

