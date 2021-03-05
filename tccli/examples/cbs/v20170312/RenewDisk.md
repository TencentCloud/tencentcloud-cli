**Example 1: 给云盘续费一个月，并设置自动续费标识**



Input: 

```
tccli cbs RenewDisk --cli-unfold-argument  \
    --DiskId disk-jwk0zvrg \
    --DiskChargePrepaid.Period 1 \
    --DiskChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "6e2e5089-244a-4102-d347-5a1f8058b1db"
    }
}
```

**Example 2: 续费实例时，需续费挂载的预付费云盘，使云盘与实例的到期时间对齐。**

实例当前到期时间为：2018-03-30 20:15:03，需续费一个月，调用本接口续费实例挂载的预付费云盘，使云盘与实例的到期时间对齐，并设置云盘为自动续费。

Input: 

```
tccli cbs RenewDisk --cli-unfold-argument  \
    --DiskId disk-jwk0zvrg \
    --DiskChargePrepaid.Period 1 \
    --DiskChargePrepaid.CurInstanceDeadline '2018-03-30 20:15:03' \
    --DiskChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "55db49cf-b9d7-da27-825b-5a02ba6884ca"
    }
}
```

