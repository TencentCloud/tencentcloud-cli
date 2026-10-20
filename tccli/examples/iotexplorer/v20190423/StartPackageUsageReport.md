**Example 1: 启用套餐用量上报请求**

启用套餐用量上报请求

Input: 

```
tccli iotexplorer StartPackageUsageReport --cli-unfold-argument  \
    --ProductId PTROMP3AOB \
    --DeviceName dev_001 \
    --ChannelId 1 \
    --ResourceId ncs-video-7d-m-xxx \
    --Operator 100012345*** \
    --Remark 
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "RequestId": "cf56eccb-3662-4eb3-9f60-ce618e749144"
    }
}
```

