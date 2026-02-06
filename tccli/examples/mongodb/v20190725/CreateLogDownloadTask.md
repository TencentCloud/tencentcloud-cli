**Example 1: 创建日志下载任务**

创建日志下载任务

Input: 

```
tccli mongodb CreateLogDownloadTask --cli-unfold-argument  \
    --InstanceId cmgo-k2p5su09 \
    --StartTime 2024-03-07 9:22:15 \
    --EndTime 2024-03-07 15:33:15 \
    --LogComponents NETWORK \
    --LogDetailParams 'client metadata'
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "1233vvae-23f9dfd"
    }
}
```

