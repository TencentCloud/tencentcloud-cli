**Example 1: 续费弹性单副本SSD硬盘**



Input: 

```
tccli cbs RenewRemoteDisk --cli-unfold-argument  \
    --DiskChargePrepaid.Period 1 \
    --RemoteDiskId rdisk-b1f7xvod
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

