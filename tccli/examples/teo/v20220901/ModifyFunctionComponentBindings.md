**Example 1: 绑定 EdgeKV 命名空间到边缘函数**

为站点 zone-3j1xw7910arp 下的边缘函数 ef-x5tuixcj 新增一个 EdgeKV 命名空间绑定，将变量名 MY_KV 绑定到命名空间 ns-011。

Input: 

```
tccli teo ModifyFunctionComponentBindings --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --FunctionId ef-x5tuixcj \
    --Operation bind \
    --FunctionComponentBindings.0.Type kv_namespace \
    --FunctionComponentBindings.0.VariableName MY_KV \
    --FunctionComponentBindings.0.KVNamespaceParameters.ZoneId zone-3j1xw7910arp \
    --FunctionComponentBindings.0.KVNamespaceParameters.Namespace ns-011
```

Output: 
```
{
    "Response": {
        "RequestId": "3fe9013c-47a3-4f0c-a660-e5f6e02faba1"
    }
}
```

