**Example 1: 创建云端审核任务**

启动SdkAppId 为 200806 指定房间（房间号为150）的云端审核任务。

房间空闲等待时间设置为30秒。
送审模式设置为，每隔5秒，送审一张视频截帧图片到ace审核商
音频每隔15秒，送审一个15s长的音频到ace审核
审核结果通过配置的回调url触达

Input: 

```
tccli trtc CreateCloudModeration --cli-unfold-argument  \
    --SdkAppId 200806 \
    --RoomId 150 \
    --RoomIdType 1 \
    --UserId inspect \
    --UserSig eJwszc3KgkAUxvF7Odv3xY6jx2KgRU1NPHMy3CnQIZEJBDxf1SulLZcs*pAAuveqIuFaeqrW2kMVyAFYogrTGbnBiScDmm2zf0*HdqoLAhxQ85dn4vMn4*N8zFT7f-aXIf3Zj0fWn78*ktBUUyJoEmHMS0ChM83AAD---1NMfA_ \
    --ModerationParams.ModerationType 1 \
    --ModerationParams.MaxIdleTime 30 \
    --ModerationParams.SliceAudio 15 \
    --ModerationParams.SliceVideo 5 \
    --ModerationParams.ModerationSupplier ace \
    --ModerationParams.ModerationSupplierParam.AppID 2501 \
    --ModerationParams.ModerationSupplierParam.SecretId ace_ugc_20521 \
    --ModerationParams.ModerationSupplierParam.SecretKey 637ae34f4069afb92xxxxxxx \
    --ModerationParams.ModerationSupplierParam.AudioBizType 2001 \
    --ModerationParams.ModerationSupplierParam.ImageBizType 2002 \
    --ModerationParams.SaveModerationFile 0 \
    --ModerationParams.CallbackAllResults 0 \
    --ModerationStorageParams.CloudModerationStorage.Vendor 0 \
    --ModerationStorageParams.CloudModerationStorage.Region ap-guangzhou \
    --ModerationStorageParams.CloudModerationStorage.Bucket av-recover-prod-1258344699 \
    --ModerationStorageParams.CloudModerationStorage.AccessKey AKIDiGYZYrugBPM3TbS2MO9dqmRp \
    --ModerationStorageParams.CloudModerationStorage.SecretKey 91w4wXswiDSQ7XfX8So31Bm6 \
    --ModerationStorageParams.CloudModerationStorage.FileNamePrefix testname \
    --ResourceExpiredHour 72
```

Output: 
```
{
    "Response": {
        "RequestId": "6c8eac0c-a46e-4002-893a-935160b43b34",
        "TaskId": "-npVqpdU7qidKD61us+k9KlbamMCLrDbczWnLoK-2OqyoZWQndib8Ma8fbGq2JxnW26LgE."
    }
}
```

