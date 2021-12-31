**Example 1: 修改磁盘续费标识**



Input: 

```
tccli lighthouse ModifyDisksRenewFlag --cli-unfold-argument  \
    --DiskIds lhdisk-qx45d7ik \
    --RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "0d5e192e-10a2-44a6-a6ce-2ac6b01f7646"
    }
}
```

