**Example 1: 设置白板快照任务回调地址**

设置白板快照任务回调地址

Input: 

```
tccli tiw SetSnapshotCallback --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --Callback https://example.com/snapshot/callback
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

