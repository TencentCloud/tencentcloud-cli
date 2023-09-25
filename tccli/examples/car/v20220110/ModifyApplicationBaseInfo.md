**Example 1: 添加修改云应用基础信息请求**



Input: 

```
tccli car ModifyApplicationBaseInfo --cli-unfold-argument  \
    --ApplicationId app-lxfdfwf \
    --ApplicationName testname \
    --ApplicationExePath App/bin/test.exe \
    --ApplicationInterList test.exe|xxx.exe \
    --ApplicationParams -b -param \
    --ApplicationBaseInfo.WindowUseType ApplicationDesktop \
    --ApplicationBaseInfo.WindowName xxx \
    --ApplicationBaseInfo.WindowClassName xxx \
    --ApplicationBaseInfo.WindowCaptureMode  \
    --ApplicationStores.0.CosBucket bucket-123456 \
    --ApplicationStores.0.CosRegion ap-guangzhou \
    --ApplicationStores.0.StoreType ARCHIVE \
    --ApplicationStores.0.StoreState OFF \
    --ApplicationStores.0.StorePath xxx \
    --ApplicationStores.1.CosBucket bucket-123456 \
    --ApplicationStores.1.CosRegion ap-guangzhou \
    --ApplicationStores.1.StoreType LOG \
    --ApplicationStores.1.StoreState ON \
    --ApplicationStores.1.StorePath xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

