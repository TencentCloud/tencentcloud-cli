**Example 1: 设置云存事件 ID 过滤规则**



Input: 

```
tccli iotexplorer ModifyTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --ChannelId 0 \
    --EventIdFilterConfig.IncludeOnly _sys_id1_data
```

Output: 
```
{
    "Response": {
        "RequestId": "e53525ed-e1c1-4748-81fa-513e89fa55c8"
    }
}
```

**Example 2: 设置输出语言**



Input: 

```
tccli iotexplorer ModifyTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --ChannelId 0 \
    --ComprehensionConfig.OutputLang zh \
    --ComprehensionConfig.AlternativeOutputLang en
```

Output: 
```
{
    "Response": {
        "RequestId": "c6d53e3e-15c5-4a56-8331-d3b680c12220"
    }
}
```

**Example 3: 设置启用视频搜索高级功能**



Input: 

```
tccli iotexplorer ModifyTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --ChannelId 0 \
    --ComprehensionConfig.EnableSearch True
```

Output: 
```
{
    "Response": {
        "RequestId": "8f0e601e-cbac-4e5c-8443-e3c1478ec5a2"
    }
}
```

**Example 4: 设置需检测的事件标签**



Input: 

```
tccli iotexplorer ModifyTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --ChannelId 0 \
    --ComprehensionConfig.DetectTypes person_climbing_fence
```

Output: 
```
{
    "Response": {
        "RequestId": "1b32234f-60bb-48dc-9791-2fffc690b035"
    }
}
```

**Example 5: 设置多摄布局**



Input: 

```
tccli iotexplorer ModifyTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --ChannelId 0 \
    --ComprehensionConfig.MultiCameraLayout Vertical,Num=2,Index=0;1
```

Output: 
```
{
    "Response": {
        "RequestId": "5f73ced5-7059-4698-ba18-3d1683f1e06a"
    }
}
```

