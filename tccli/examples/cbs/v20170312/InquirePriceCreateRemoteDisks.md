**Example 1: 查询创建弹性单副本SSD硬盘的价格（后付费）**



Input: 

```
tccli cbs InquirePriceCreateRemoteDisks --cli-unfold-argument  \
    --DiskChargeType POSTPAID_BY_HOUR \
    --DiskSize 3000
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

**Example 2: 查询创建弹性单副本SSD硬盘的价格（预付费）**



Input: 

```
tccli cbs InquirePriceCreateRemoteDisks --cli-unfold-argument  \
    --DiskChargePrepaid.Period 1 \
    --DiskChargeType PREPAID \
    --DiskCount 1 \
    --DiskSize 2000
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

