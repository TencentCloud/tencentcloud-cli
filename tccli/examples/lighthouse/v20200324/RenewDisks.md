**Example 1: 续费云硬盘**

续费云硬盘

Input: 

```
tccli lighthouse RenewDisks --cli-unfold-argument  \
    --DiskIds lhdisk-ovav4qmi \
    --RenewDiskChargePrepaid.CurInstanceDeadline 2023-09-09 23:59:59 \
    --AutoVoucher True
```

Output: 
```
{
    "Response": {
        "RequestId": "c139e106-cdb2-4923-8f1e-ea1dc4fe3a47"
    }
}
```

