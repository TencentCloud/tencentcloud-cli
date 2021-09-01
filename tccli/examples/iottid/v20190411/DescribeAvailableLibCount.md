**Example 1: 查询软加固订单可空发数量-2**

订单编号p8ZcXGuqus，类型为软加固产品，历史上传1000个硬件标识码，尚未空发过任何软加固TID。

Input: 

```
tccli iottid DescribeAvailableLibCount --cli-unfold-argument  \
    --OrderId p8ZcXGuqus
```

Output: 
```
{
    "Response": {
        "RequestId": "006b23f0-d768-439e-99e9-1c09af0432af",
        "Quantity": 1000
    }
}
```

**Example 2: 查询软加固订单可空发数量**

订单编号p8ZcXGuqus，类型为软加固产品，历史上传1000个硬件标识码，已通过DeliverTids空发接口发送100个TID，剩余900未空发。

Input: 

```
tccli iottid DescribeAvailableLibCount --cli-unfold-argument  \
    --OrderId p8ZcXGuqus
```

Output: 
```
{
    "Response": {
        "RequestId": "006b23f0-d768-439e-99e9-1c09af0432af",
        "Quantity": 900
    }
}
```

