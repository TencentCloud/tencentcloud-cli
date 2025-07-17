**Example 1: 创建切片任务**

启动SdkAppId 为 200806 指定房间（房间号为150）的云端切片任务。

房间空闲等待时间设置为30秒。
切片模式设置为音频切片+视频截帧
音频隔15秒切片一次
视频隔5秒，截帧一次

Input: 

```
tccli trtc CreateCloudSliceTask --cli-unfold-argument  \
    --SdkAppId 200806 \
    --RoomId 150 \
    --UserId inspect \
    --UserSig eJxxxv3xY6jx2KgRU1NPHMy3CnQIZEJBDxf1SulLZcs*pAAuveqIuFaeqrW2kMVyAFYogrTGbnBiScDmm2zf0*HdqoLAhxQ85dn4vMn4*N8zFT7f-aXIf3Zj0fWn78*ktBUUyJoEmHMS0ChM83AAD---1NMfA_ \
    --SliceParams.SliceType 3 \
    --SliceParams.MaxIdleTime 30 \
    --SliceParams.SliceAudio 15 \
    --SliceParams.SliceVideo 5 \
    --SliceStorageParams.CloudSliceStorage.Vendor 0 \
    --SliceStorageParams.CloudSliceStorage.Region ap-guangzhou \
    --SliceStorageParams.CloudSliceStorage.Bucket av-recover-prod-1258344699 \
    --SliceStorageParams.CloudSliceStorage.AccessKey AKIDiGYZYrugBPM3TbS2MO9dqxxx \
    --SliceStorageParams.CloudSliceStorage.SecretKey 91w4wXswiDSQ7XfX8So31xxx \
    --SliceStorageParams.CloudSliceStorage.FileNamePrefix prefix1 \
    --RoomIdType 1 \
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

