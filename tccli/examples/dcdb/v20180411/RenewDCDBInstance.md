**Example 1: 续费分布式数据库实例**



Input: 

```
tccli dcdb RenewDCDBInstance --cli-unfold-argument  \
    --InstanceId dcdbt-avw0207d \
    --Period 1 \
    --AutoVoucher false
```

Output: 
```
{
    "Response": {
        "RequestId": "e87698f2-4576-730e-cba6-59fabe133cf8",
        "DealName": "20171103110253"
    }
}
```

