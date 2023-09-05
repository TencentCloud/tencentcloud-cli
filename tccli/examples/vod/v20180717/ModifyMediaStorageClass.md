**Example 1: 将媒体文件从标准存储修改为低频存储**

将媒体文件从标准存储修改为低频存储

Input: 

```
tccli vod ModifyMediaStorageClass --cli-unfold-argument  \
    --FileIds 5285485487985271487 \
    --StorageClass STANDARD_IA
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

