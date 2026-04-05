**Example 1: 修改 EdgeKV 命名空间描述**

修改站点 zone-3j1xw7910arp 下命名空间 ns-011 的描述信息为 second remark。

Input: 

```
tccli teo ModifyEdgeKVNamespace --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --Namespace ns-011 \
    --Remark second remark
```

Output: 
```
{
    "Response": {
        "RequestId": "306476ec-7647-482e-a7c2-f722e4f05813"
    }
}
```

