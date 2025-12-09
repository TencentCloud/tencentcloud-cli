**Example 1: 成功**



Input: 

```
tccli lke GenerateOrderSign --cli-unfold-argument  \
    --GoodsJson {"uin":"","ownerUin":"","appId":0,"goods":[{"purpose":"autoRenew","regionId":47,"payMode":1,"action":"renew","zoneId":100001,"type":"sp_jifei_prepay_resource","goodsNum":1,"projectId":80000,"platform":1,"goodsDetail":{"buyr":"test","resourceId":"4791676932101","curDeadline":"2024-10-26 08:53:14","pid":1100100,"fromAutoRenew":1,"autoRenewFlag":0,"queryFlowType":1,"productInfo":[{"name":"计费测试商品新购","value":"jfcs"}],"succ":1,"goodsRnum":1,"RTimeUnit":"m","action":"purchase","RTimeSpan":2,"timeSpan":1,"region":47,"sv_jifei_prepay_resource_3":1,"goodsNum":1,"timeUnit":"m"}}]}
```

Output: 
```
{
    "Response": {
        "RequestId": "reqid",
        "GoodsJson": "{\"appId\":0,\"auth\":{\"nonce\":\"eUtBtu9hGCWmOFdy\",\"secretId\":\"239529489f1a922ae30331b7a442d9821769d936\",\"signature\":\"EKXyjyAbyPEI0NBqjwuo0DMBdFkX9sjGDdxfDgYqfcQ=\",\"timestamp\":1741762322,\"version\":\"3.0\"},\"goods\":[{\"action\":\"renew\",\"goodsDetail\":{\"RTimeSpan\":2,\"RTimeUnit\":\"m\",\"action\":\"purchase\",\"autoRenewFlag\":0,\"buyr\":\"test\",\"curDeadline\":\"2024-10-26 08:53:14\",\"fromAutoRenew\":1,\"goodsNum\":1,\"goodsRnum\":1,\"pid\":1100100,\"productInfo\":[{\"name\":\"计费测试商品新购\",\"value\":\"jfcs\"}],\"queryFlowType\":1,\"region\":47,\"resourceId\":\"4791676932101\",\"succ\":1,\"sv_jifei_prepay_resource_3\":1,\"timeSpan\":1,\"timeUnit\":\"m\"},\"goodsNum\":1,\"payMode\":1,\"platform\":1,\"projectId\":80000,\"purpose\":\"autoRenew\",\"regionId\":47,\"type\":\"sp_jifei_prepay_resource\",\"zoneId\":100001}],\"ownerUin\":\"\",\"platform\":1,\"uin\":\"\"}"
    }
}
```

