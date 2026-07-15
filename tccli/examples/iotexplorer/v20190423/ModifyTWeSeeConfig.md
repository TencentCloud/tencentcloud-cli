**Example 1: 对指定设备开启 TWeSee 摘要与搜索能力**

已接入 IoT 云存的设备开启 TWeSee 摘要与搜索能力

Input: 

```
tccli iotexplorer ModifyTWeSeeConfig --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev001 \
    --EnableSummary True \
    --EnableSearch True
```

Output: 
```
{
    "Response": {
        "RequestId": "2dbdcb8c-d8cb-4f9d-a491-ff0dd3bb53b6"
    }
}
```

**Example 2: 对指定设备开启 TWeSee 摘要能力**

已接入 IoT 云存的设备开启 TWeSee 摘要能力

Input: 

```
tccli iotexplorer ModifyTWeSeeConfig --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev001 \
    --EnableSummary True
```

Output: 
```
{
    "Response": {
        "RequestId": "2dbdcb8c-d8cb-4f9d-a491-ff0dd3bb53b6"
    }
}
```

**Example 3: 对指定设备开启 TWeSee 摘要能力并添加更多的检测标签**

已接入 IoT 云存的设备开启 TWeSee 摘要能力，并且传入扩展的事件/行为检测标签

Input: 

```
tccli iotexplorer ModifyTWeSeeConfig --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev001 \
    --EnableSummary True \
    --EnableSearch True \
    --SummaryConfig.DetectTypes baby_crying
```

Output: 
```
{
    "Response": {
        "RequestId": "2dbdcb8c-d8cb-4f9d-a491-ff0dd3bb53b6"
    }
}
```

