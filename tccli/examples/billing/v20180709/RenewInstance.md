**Example 1: 续费实例**

续费主机安全-日志分析实例

Input: 

```
tccli billing RenewInstance --cli-unfold-argument  \
    --ClientToken 46E6BF87-AF23-4710-8C82-21032D5F337F \
    --RegionCode ap-guangzhou \
    --InstanceId ********* \
    --ProductCode p_yunjing \
    --SubProductCode sp_yunjing_vas
```

Output: 
```
{
    "Response": {
        "OrderIdList": [
            "20251201*********"
        ],
        "RequestId": "9792e525-4002-4fb2-8a35-74ebf854bee7"
    }
}
```

