**Example 1: 商品识别检测请求成功**



Input: 

```
tccli tiia DetectProduct --cli-unfold-argument  \
    --ImageUrl http://a.vpimg2.com/upload/merchandise/41498/CABBEEN-3030701301-1.jpg
```

Output: 
```
{
    "Response": {
        "Products": [
            {
                "Name": "男士西服套装",
                "Parents": "服饰内衣-男装",
                "Confidence": 59,
                "XMin": 336,
                "YMin": 191,
                "XMax": 799,
                "YMax": 775
            },
            {
                "Name": "休闲鞋",
                "Parents": "鞋靴-时尚女鞋",
                "Confidence": 40,
                "XMin": 466,
                "YMin": 1209,
                "XMax": 695,
                "YMax": 1377
            }
        ],
        "RequestId": "2bd4243f-4d26-4246-a5f4-0f2dbc730d62"
    }
}
```

