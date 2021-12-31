**Example 1: 查询磁盘操作限制列表**



Input: 

```
tccli lighthouse DescribeDisksDeniedActions --cli-unfold-argument  \
    --DiskIds lhdisk-eobj8huv
```

Output: 
```
{
    "Response": {
        "DiskDeniedActionSet": [
            {
                "DiskId": "lhdisk-eobj8huv",
                "DeniedActions": [
                    {
                        "Action": "DetachDisks",
                        "Code": "UnsupportedOperation.InvalidDiskState",
                        "Message": "磁盘 `lhdisk-eobj8huv` 处于 `待挂载` 状态中，不支持该操作。"
                    }
                ]
            }
        ],
        "RequestId": "fd7fcb32-d48f-4d0e-ab33-e4985fc6e647"
    }
}
```

