**Example 1: 更新产品动态注册**

更新产品动态注册

Input: 

```
tccli iotcloud UpdateProductDynamicRegister --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --RegisterType 0 \
    --RegisterLimit 10
```

Output: 
```
{
    "Response": {
        "RegisterType": 0,
        "ProductSecret": "xxxx",
        "RegisterLimit": 10000,
        "RequestId": "d15b72a9-ab2b-4906-9632-52f7a31932a9"
    }
}
```

