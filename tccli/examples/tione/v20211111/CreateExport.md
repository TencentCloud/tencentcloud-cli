**Example 1: 创建日志下载任务**

创建任务式建模训练任务，Notebook，在线服务和批量预测任务日志下载任务API

Input: 

```
tccli tione CreateExport --cli-unfold-argument  \
    --Service TRAIN \
    --ServiceId train-1051209973208673664-7zimubsiul1c \
    --StartTime 2022-01-10T12:15:03+08:00 \
    --EndTime 2022-01-11T12:15:03+08:00 \
    --Format csv
```

Output: 
```
{
    "Response": {
        "ExportId": "57196a6a-7622-47be-bc92-d2ebea959a0f",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

