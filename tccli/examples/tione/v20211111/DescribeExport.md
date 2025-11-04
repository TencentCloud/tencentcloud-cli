**Example 1: 查询日志下载任务详情**

查看任务式建模训练任务，Notebook，在线服务和批量预测任务日志下载任务状态API

Input: 

```
tccli tione DescribeExport --cli-unfold-argument  \
    --ExportId 57196a6a-7622-47be-bc92-d2ebea959a0f
```

Output: 
```
{
    "Response": {
        "ExportId": "export-57196a6a-7622-47be-bc92-d2ebea959a0f",
        "FileName": "train-1051209973208673664-7zimubsiul1c_1610001073.tar.gz",
        "CosPath": "https://clstest01-xxxxxx.cos.ap-shanghai.myqcloud.com/xxxxxx",
        "CreateTime": "2020-08-08 12:12:12",
        "FileSize": "6112993",
        "Status": "Completed",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

