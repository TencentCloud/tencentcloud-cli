**Example 1: 查询边缘函数组件绑定列表**

查询站点 zone-3j1xw7910arp 下边缘函数 ef-x5tuixcj 的组件绑定列表，从第 0 条开始，每页返回 10 条。

Input: 

```
tccli teo DescribeFunctionComponentBindings --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --FunctionId ef-x5tuixcj \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "FunctionComponentBindings": [
            {
                "KVNamespaceParameters": {
                    "Namespace": "ns-011",
                    "ZoneId": "zone-3j1xw7910arp"
                },
                "Type": "kv_namespace",
                "VariableName": "MY_KV"
            }
        ],
        "TotalCount": 1,
        "RequestId": "34da5ee4-18b8-4d18-9354-907df99d4234"
    }
}
```

