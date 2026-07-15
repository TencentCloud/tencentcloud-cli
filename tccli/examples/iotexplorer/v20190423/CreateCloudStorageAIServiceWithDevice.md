**Example 1: 创建设备并开通视频集锦（Diary）标准版月套餐**



Input: 

```
tccli iotexplorer CreateCloudStorageAIServiceWithDevice --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev001 \
    --PackageId diary_basic \
    --ServiceType Diary
```

Output: 
```
{
    "Response": {
        "RequestId": "ae7e93ab-6ef0-44db-8a17-125fbe25209a"
    }
}
```

**Example 2: 创建设备并开通视频浓缩（Daily Highlight）高级版月套餐**



Input: 

```
tccli iotexplorer CreateCloudStorageAIServiceWithDevice --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev001 \
    --PackageId diary_hl_premium \
    --ServiceType SimpleHighlight
```

Output: 
```
{
    "Response": {
        "RequestId": "ae7e93ab-6ef0-44db-8a17-125fbe25209a"
    }
}
```

