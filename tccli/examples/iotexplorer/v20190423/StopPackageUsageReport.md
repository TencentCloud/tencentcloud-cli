**Example 1: 停用套餐用量上报请求**

停用套餐用量上报请求

Input: 

```
tccli iotexplorer StopPackageUsageReport --cli-unfold-argument  \
    --ProductId PTROMP3AOB \
    --DeviceName dev_001 \
    --ChannelId 1 \
    --Operator 100012345678 \
    --Remark  \
    --MediaType video
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "cf56eccb-3662-4eb3-9f60-ce618e749144"
    }
}
```

