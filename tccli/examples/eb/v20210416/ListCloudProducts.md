**Example 1: 获取云产品列表**

获取云产品列表

Input: 

```
tccli eb ListCloudProducts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ffd4aae2-c29e-40a8-b18c-037a17ed810c",
        "CloudProducts": [
            {
                "ProductName": "云服务器",
                "ProductType": "cvm",
                "Type": "Cloud"
            }
        ]
    }
}
```

