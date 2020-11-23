**Example 1: 查询产品列表**



Input: 

```
tccli cr QueryProducts --cli-unfold-argument  \
    --Module Products \
    --Operation QueryProducts \
    --InstanceId ins-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ProductList": [
            {
                "ProductCode": "Pxxx",
                "SceneType": "A",
                "ProductName": "测试产品",
                "ProductStatus": 0,
                "ProductId": "pdt-xxxxxx"
            }
        ]
    }
}
```

