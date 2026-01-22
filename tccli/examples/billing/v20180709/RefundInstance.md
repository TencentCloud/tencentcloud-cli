**Example 1: 退订实例**

退订主机安全-旗舰版实例

Input: 

```
tccli billing RefundInstance --cli-unfold-argument  \
    --ClientToken 46E6BF87-AF23-4710-8C82-21032D5F389F \
    --RegionCode ap-guangzhou \
    --ProductCode p_yunjing \
    --SubProductCode sp_yunjing_0014552 \
    --InstanceId *********
```

Output: 
```
{
    "Response": {
        "OrderIdList": [
            "20251201*************"
        ],
        "RequestId": "41ac9a14-b2a3-4af5-a66f-baa56113ea4a"
    }
}
```

