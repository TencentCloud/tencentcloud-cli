**Example 1: 创建Dspm申请单**



Input: 

```
tccli csip CreateDspmApplyOrder --cli-unfold-argument  \
    --AssetId cdb-c2thbt00 \
    --Subject pid_mwnmmjiz \
    --ApproverUin 100000 \
    --Reason for test \
    --ManagerType 0 \
    --ApplyType 0
```

Output: 
```
{
    "Response": {
        "OrderId": "order-yzfhzjvk",
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

