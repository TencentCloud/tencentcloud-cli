**Example 1: 获取合同详情嵌入WEB链接**

	
获取合同详情嵌入WEB链接

Input: 

```
tccli ess CreateEmbedWebUrl --cli-unfold-argument  \
    --Operator.UserId yDwJsUUckpkjss52UCW2se8TOSLS4tEP \
    --BusinessId aDRt2UUgygqxyp9yUuO4zjEwqXwsIljY \
    --EmbedType PREVIEW_FLOW_DETAIL
```

Output: 
```
{
    "Response": {
        "WebUrl": "https://embed.test.qian.tencent.cn//contract-details?embed=1&code=yDwFJUUckpsm2e3xU6LVMFEMw1e4YIkb&channel=TENCENTCLOUD&businessId=yDwFFUUckps75s4pUEmvMvC8iyRPYukZ&businessType=DOCUMENT&scene=SINGLEPAGE",
        "RequestId": "s1694572778289857146"
    }
}
```

**Example 2: 获取生成印章嵌入WEB链接**

获取生成印章嵌入WEB链接

Input: 

```
tccli ess CreateEmbedWebUrl --cli-unfold-argument  \
    --Operator.UserId yDwJsUUckpkjss52UCW2se8TOSLS4tEP \
    --EmbedType CREATE_SEAL \
    --Agent.ProxyOrganizationId 
```

Output: 
```
{
    "Response": {
        "WebUrl": "https://embed.qian.tencent.cn/seal-create?embed=1&code=yDwgzUUckp12yp52UEHWYmLCd041eukw&channel=TENCENTCLOUD&businessType=SEAL",
        "RequestId": "s1694572778289857145"
    }
}
```

**Example 3: 获取合同详情嵌入WEB链接-指定可查看控件**

获取合同详情嵌入WEB链接-指定可查看控件

Input: 

```
tccli ess CreateEmbedWebUrl --cli-unfold-argument  \
    --Operator.UserId yDwJsUUckpkjss52UCW2se8TOSLS4tEP \
    --BusinessId aDRt2UUgygqxyp9yUuO4zjEwqXwsIljY \
    --EmbedType PREVIEW_FLOW_DETAIL \
    --Option.ShowFlowDetailComponent True
```

Output: 
```
{
    "Response": {
        "WebUrl": "https://embed.test.qian.tencent.cn//contract-details?embed=1&code=yDwFJUUckpsm2e3xU6LVMFEMw1e4YIkb&channel=TENCENTCLOUD&businessId=yDwFFUUckps75s4pUEmvMvC8iyRPYukZ&showComponent=1&businessType=DOCUMENT&scene=SINGLEPAGE",
        "RequestId": "s1694572778289857146"
    }
}
```

**Example 4: 获取合同详情嵌入Web链接失败，是因为对应的签署流程不存在。**

获取合同详情嵌入Web链接失败，是因为对应的签署流程不存在。

Input: 

```
tccli ess CreateEmbedWebUrl --cli-unfold-argument  \
    --Operator.UserId yDwJsUUckpkjss52UCW2se8TOSLS4tEP \
    --BusinessId aDRt2UUgygqxyp9yUuO4zjEwqXwsIljY \
    --EmbedType PREVIEW_FLOW_DETAIL
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.DataNotFlound",
            "Message": "未查询到流程"
        },
        "RequestId": "s1694572778289857144"
    }
}
```

