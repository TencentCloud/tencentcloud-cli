**Example 1: 修改应用配置信息**

客户希望可以通过Api批量修改应用的配置信息

Input: 

```
tccli apm ModifyGeneralApmApplicationConfig --cli-unfold-argument  \
    --Tags.0.Key UrlConvergence \
    --Tags.0.Value RPCServer/market.MarketServiceleetcode9(.*?) \
    --Tags.1.Key UrlConvergenceThreshold \
    --Tags.1.Value 600 \
    --Tags.2.Key UrlConvergenceSwitch \
    --Tags.2.Value 1 \
    --Tags.3.Key AgentEnable \
    --Tags.3.Value true \
    --ServiceNames stock-service profile-service28 profile-service08 \
    --InstanceId apm-059oXBfTL
```

Output: 
```
{
    "Response": {
        "RequestId": "test-test-test0980990"
    }
}
```

