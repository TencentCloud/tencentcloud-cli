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
    --ApplicationStores.0.CosBucket application-log-1300543887 \
    --ApplicationStores.0.CosRegion ap-guangzhou \
    --ApplicationStores.0.StoreType LOG \
    --ApplicationStores.0.StoreState ON \
    --ApplicationStores.0.StorePath WindowsNoEditor705/log
```

Output: 
```
{
    "Response": {
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

