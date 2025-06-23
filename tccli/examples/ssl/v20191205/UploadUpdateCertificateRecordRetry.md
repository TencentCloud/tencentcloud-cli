**Example 1: 云资源更新（证书ID不变）重试部署记录 - 全部失败记录重试**



Input: 

```
tccli ssl UploadUpdateCertificateRecordRetry --cli-unfold-argument  \
    --DeployRecordId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "79b4dae4-51a7-4345-9b2b-0c6a29f69291"
    }
}
```

**Example 2: 云资源更新（证书ID不变）重试回滚部署记录 - 指定失败记录重试**



Input: 

```
tccli ssl UploadUpdateCertificateRecordRetry --cli-unfold-argument  \
    --DeployRecordDetailId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "79b4dae4-51a7-4345-9b2b-0c6a29f69291"
    }
}
```

