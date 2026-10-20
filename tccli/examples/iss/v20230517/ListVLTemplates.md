**Example 1: 成功示例**



Input: 

```
tccli iss ListVLTemplates --cli-unfold-argument  \
    --Name 明厨亮灶识别模板 \
    --AnalysisMode image \
    --CaptureType realtime \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AIModel": "IVC-G",
                "AnalysisMode": "image",
                "CreatedAt": "2026-07-27 15:14:28",
                "Describe": "厨师帽和口罩识别",
                "ImageConfig": {
                    "Interval": 10,
                    "MultiMode": null,
                    "Type": 1
                },
                "IsUsed": false,
                "Name": "明厨亮灶识别模板",
                "Prompt": "你是餐饮后厨着装规范检查模型，仅检查厨师帽、口罩两项。\n## 合规标准\n- 厨师帽：佩戴且完全覆盖头发（高筒帽/网帽/布帽均合规）；未戴或发丝外露为不合规\n- 口罩：覆盖鼻梁至下颌（蓝/白医用口罩、透明面罩均合规）；拉下巴/挂耳朵/仅遮嘴为不合规\n## 输出\n紧凑JSON，无markdown/换行/空格。\n- total_staff：int，后厨人员总数\n- hat：{\"compliant\":int,\"non_compliant\":int,\"not_wearing\":int}，帽子合规/不规范/未戴人数\n- mask：{\"compliant\":int,\"non_compliant\":int,\"not_wearing\":int}，口罩合规/不规范/未戴人数",
                "Times": [
                    {
                        "BeginTime": "00:00:00",
                        "EndTime": "23:59:59",
                        "WeekDay": 1
                    }
                ],
                "UpdatedAt": "2026-07-27 15:14:28",
                "VLTemplateId": "VTa911*************************6c2"
            }
        ],
        "TotalCount": 1,
        "RequestId": "75677860-9600-494e-b0d9-ba61cb74cf4d"
    }
}
```

