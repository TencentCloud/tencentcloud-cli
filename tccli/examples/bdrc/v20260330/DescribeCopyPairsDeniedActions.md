**Example 1: 查询复制对掩码**



Input: 

```
tccli bdrc DescribeCopyPairsDeniedActions --cli-unfold-argument  \
    --CopyPairIds cvmcopypair-ibd2jvbj \
    --CopyPairType INSTANCE
```

Output: 
```
{
    "Response": {
        "CopyPairDeniedActionSet": [
            {
                "CopyPairId": "cvmcopypair-ibd2jvbj",
                "DeniedActions": [
                    {
                        "Action": "StopDiskCopyPairTasks",
                        "Code": "UnsupportedOperation.CopyPairStateError",
                        "Message": "复制对(cvmcopypair-ibd2jvbj)的状态不支持当前操作"
                    }
                ]
            }
        ],
        "RequestId": "c30d60d4-c201-440b-a562-c0738983727d"
    }
}
```

