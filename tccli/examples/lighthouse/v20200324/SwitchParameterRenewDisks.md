**Example 1: 续费磁盘订单参数转换**

续费磁盘订单参数转换

Input: 

```
tccli lighthouse SwitchParameterRenewDisks --cli-unfold-argument  \
    --DiskIds lhdisk-eobj8huv \
    --RenewDiskChargePrepaid.Period 1 \
    --RenewDiskChargePrepaid.CurInstanceDeadline 2022-05-05 19:20:20 \
    --RenewDiskChargePrepaid.TimeUnit m
```

Output: 
```
{
    "Response": {
        "DiskOrder": "",
        "RequestId": "0d5e192e-10a2-44a6-a6ce-2ac6b01f7646"
    }
}
```

