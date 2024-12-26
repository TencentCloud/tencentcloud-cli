**Example 1: 创建云应用项目示例**

用于创建云应用项目

Input: 

```
tccli car CreateApplicationProject --cli-unfold-argument  \
    --Name project_name \
    --ApplicationId app-s324or12 \
    --Type S1 \
    --IsPreload True \
    --ApplicationParams -params \
    --Resolution 1920x1080 \
    --ProjectType EXCLUSIVE \
    --FPS 0 \
    --PreloadDuration 10s \
    --ReconnectTimeout 20s \
    --MinBitrate 0 \
    --MaxBitrate 10
```

Output: 
```
{
    "Response": {
        "ProjectId": "cap-lhze1cs5",
        "RequestId": "25b6f399-bd7c-4e5e-99a3-9a6f4b11e1b7"
    }
}
```

