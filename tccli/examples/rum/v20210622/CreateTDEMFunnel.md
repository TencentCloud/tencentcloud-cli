**Example 1: 示例**



Input: 

```
tccli rum CreateTDEMFunnel --cli-unfold-argument  \
    --AppId 1****2 \
    --FunnelName 下单支付 \
    --Steps.0.StepName 进入首页 \
    --Steps.0.PagePattern 进入首页 \
    --Steps.0.PageMatchMode exact \
    --Description enter page \
    --Status active \
    --Source manual
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InvalidParameter\",\"Message\":\"步骤数必须在2到20之间\"}",
        "RequestId": "62b1ae8e-b233-4248-b948-bb972ead0db0"
    }
}
```

