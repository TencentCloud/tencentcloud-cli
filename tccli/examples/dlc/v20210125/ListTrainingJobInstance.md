**Example 1: 获取训练作业配置的列表**



Input: 

```
tccli dlc ListTrainingJobInstance --cli-unfold-argument  \
    --Page 1 \
    --PageSize 3 \
    --Filters.0.Name specId \
    --Filters.0.Values raytrain-spec-tgpuaz-i3fg \
    --SortFields.0.Field createTime \
    --SortFields.0.Order desc \
    --StartTime 1767196800000 \
    --EndTime 1782835200000
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": 1782127080564,
                "Creator": "700002655693",
                "HistoryUrl": "https://cls-pdb9lgk2.tcray-gateway.ap-guangzhou.cloud.tencent.com/dlc-p-ikzmoqyv/rayjob-20260622191756-22su/",
                "InstanceId": "rayjob-20260622191756-22su",
                "JobCreateTime": 1782127081636,
                "JobRunningTime": 5053576,
                "Priority": 5,
                "SpecId": "raytrain-spec-tgpuaz-i3fg",
                "SpecName": "v1-sft-sft-data-lora-p13g",
                "Status": "PENDING"
            }
        ],
        "Page": 1,
        "PageSize": 3,
        "Total": 9,
        "TotalPages": 3,
        "RequestId": "031bdecf-1cad-4dda-a192-4d81852bdfcb"
    }
}
```

