**Example 1: 删除策略及其插件投影**

仅删除策略，业务服务继续保留。 这是说明性示例，未执行真实资源操作；响应字段以目标环境实际部署版本为准。

Input: 

```
tccli tse DeleteAIGWCustomGuardrailPolicy --cli-unfold-argument  \
    --GatewayId gateway-12345678 \
    --PolicyId 11111111-1111-4111-8111-111111111111
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "FailedResources": []
        },
        "RequestId": "77777777-7777-4777-8777-777777777777"
    }
}
```

