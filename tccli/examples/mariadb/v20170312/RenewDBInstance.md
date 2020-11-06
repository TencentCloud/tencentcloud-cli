**Example 1: 续费云数据库实例**



Input: 

```
tccli mariadb RenewDBInstance --cli-unfold-argument  \
    --InstanceId tdsql-avw0207d \
    --Period 1 \
    --AutoVoucher true
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

