**Example 1: 创建实例**

创建主机安全-日志分析实例，购买数量1，购买时长1个月，并设置自动续费。

Input: 

```
tccli billing CreateInstance --cli-unfold-argument  \
    --ClientToken 46E6BF87-AF23-4710-8C82-21032D5F985F \
    --ProductCode p_yunjing \
    --SubProductCode sp_yunjing_vas \
    --RegionCode ap-guangzhou \
    --ZoneCode ap-guangzhou-1 \
    --PayMode PrePay \
    --Parameter {"pid":1005305,"productCode":"p_yunjing","subProductCode":"sp_yunjing_vas","sv_yunjing_vas_la":"50","timeSpan":1,"timeUnit":"m"} \
    --Quantity 1 \
    --Period 1 \
    --PeriodUnit m \
    --ProjectId 0 \
    --RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "OrderId": "20251201********",
        "InstanceIdList": [
            "*******"
        ],
        "RequestId": "9792e525-4002-4fb2-8a35-74ebf854bee7"
    }
}
```

