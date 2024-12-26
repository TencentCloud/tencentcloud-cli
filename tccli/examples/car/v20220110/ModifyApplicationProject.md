**Example 1: 修改云应用项目请求**

用于修改云应用项目

Input: 

```
tccli car ModifyApplicationProject --cli-unfold-argument  \
    --IsPreload True \
    --ProjectId cap-lhze1cs5 \
    --ApplicationParams -params \
    --Name project_name \
    --Type L1 \
    --FPS 0 \
    --PreloadDuration 10s \
    --ReconnectTimeout 20s \
    --MinBitrate 0 \
    --MaxBitrate 10 \
    --DisableVideoCodecs H265
```

Output: 
```
{
    "Response": {
        "RequestId": "25b6f399-bd7c-4e5e-99a3-9a6f4b11e1b7"
    }
}
```

