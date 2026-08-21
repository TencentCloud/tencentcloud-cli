**Example 1: 配置用户同步**

配置用户同步

Input: 

```
tccli csip ModifyBaselineSyncConf --cli-unfold-argument  \
    --SyncConf.AutoSync True \
    --SyncConf.TargetAppidList 200000000 \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "RequestId": "36c1a57c-e638-452d-8748-81029f7e2f58"
    }
}
```

