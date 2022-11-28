**Example 1: 活动商品下单取消扣减商品配额**



Input: 

```
tccli opc CancelActivityGoodsQuotaDeduction --cli-unfold-argument  \
    --DealUin  \
    --DealResult {"code": 10028, "errCode": null, "errMsg": "error", "msg": "", "returnCode": 0, "returnValue": "ok"}
```

Output: 
```
{
    "Response": {
        "RequestId": "scbnohgb-wkaf-m3nt-yus0-zyaafyk4ch4z"
    }
}
```

