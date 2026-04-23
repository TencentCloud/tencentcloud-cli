**Example 1: 实例升级**



Input: 

```
tccli cdb UpgradeDBInstance --cli-unfold-argument  \
    --InstanceId cdb-bxtgirxj \
    --Memory 2000 \
    --Volume 110 \
    --ProtectMode 1 \
    --WaitSwitch 1
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "ec58aec9-05d6185f-02dad5fa-b67f1dff",
        "DealIds": [
            "20260423753022636848431"
        ],
        "RequestId": "fe1a3323-5968-40c1-939e-56f659c2f3c5"
    }
}
```

