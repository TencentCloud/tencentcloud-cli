**Example 1: 创建控制台匿名分享请求示例**

创建控制台检索页/仪表盘免登陆分享站点

Input: 

```
tccli cls CreateConsoleSharing --cli-unfold-argument  \
    --SharingConfig.Name my-sharing \
    --SharingConfig.Type 1 \
    --SharingConfig.VerifyCode lEC0V0 \
    --SharingConfig.DurationMilliseconds 1800000 \
    --SharingConfig.NowTime 1706787306086 \
    --SharingConfig.IsLockTimeRange True \
    --SharingConfig.IsLockQuery True \
    --SharingConfig.Params.0.Name query \
    --SharingConfig.Resources qcs::cls:ap-guangzhou:uin/10000000001:topic/c1306921-2180-3e45-9azb-31d12217871e6
```

Output: 
```
{
    "Response": {
        "SharingUrl": "https://clsshare.tencent-cloud.com/s/13cez28h",
        "SharingId": "13cez28h",
        "RequestId": "714cf720-43e9-460b-bd9a-42a193ca3d94"
    }
}
```

