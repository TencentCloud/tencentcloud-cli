**Example 1: 查询续费弹性单副本SSD硬盘的价格**



Input: 

```
tccli cbs InquirePriceRenewRemoteDisks --cli-unfold-argument  \
    --DiskChargePrepaidSet.0.Period 1 \
    --RemoteDiskIds rdisk-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

