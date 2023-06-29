**Example 1: 创建一个同步任务**

创建一个同步任务

Input: 

```
tccli dts CreateSyncJob --cli-unfold-argument  \
    --Count 1 \
    --Specification Standard \
    --PayMode PrePay \
    --DstDatabaseType mysql \
    --DstRegion ap-guangzhou \
    --SrcDatabaseType mysql \
    --SrcRegion ap-guangzhou \
    --ExistedJobId sync-xascasas
```

Output: 
```
{
    "Response": {
        "JobIds": [
            "sync-eivc87yk"
        ],
        "RequestId": "03a378be-372a-478b-beb7-19e4dd5027e2"
    }
}
```

