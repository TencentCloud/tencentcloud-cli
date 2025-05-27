**Example 1: 查询安灯工具支持的产品列表**



Input: 

```
tccli monitor DescribeAndonToolProducts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ProductList": [
            {
                "Product": "abc",
                "ProductShowName": "abc",
                "Namespace": "abc",
                "ViewName": "abc",
                "ViewNameShowName": "abc",
                "APIDimensionKeys": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

