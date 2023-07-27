**Example 1: 获取合同详情嵌入WEB链接**

	
获取合同详情嵌入WEB链接

Input: 

```
tccli ess CreateEmbedWebUrl --cli-unfold-argument  \
    --Operator.UserId 1 \
    --BusinessId aDRt2UUgygqxyp9yUuO4zjEwqXwsIljY \
    --EmbedType PREVIEW_FLOW_DETAIL
```

Output: 
```
{
    "Response": {
        "WebUrl": "https://embed.test.qian.tencent.cn//contract-details?embed=1&code=yDwFJUUckpsm2e3xU6LVMFEMw1e4YIkb&channel=TENCENTCLOUD&businessId=yDwFFUUckps75s4pUEmvMvC8iyRPYukZ&businessType=DOCUMENT&scene=SINGLEPAGE",
        "RequestId": "s123456789"
    }
}
```

