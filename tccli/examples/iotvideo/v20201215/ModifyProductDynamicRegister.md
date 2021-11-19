**Example 1: 修改产品动态注册**



Input: 

```
tccli iotvideo ModifyProductDynamicRegister --cli-unfold-argument  \
    --ProductId KO9JAFB9W \
    --RegisterType 2 \
    --RegisterLimit 50
```

Output: 
```
{
    "Response": {
        "ProductSecret": "Secret",
        "RegisterLimit": 50,
        "RegisterType": 2,
        "RequestId": "1aa7421b-f69b-4ea9-acf5-4bf22681f3b1"
    }
}
```

