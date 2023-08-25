**Example 1: 敏感数据导出**

创建敏感数据导出任务

Input: 

```
tccli dsgc ExportAssetDetailData --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --ComplianceId 1 \
    --MetaDataType cos
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "ExportTaskId": 44
    }
}
```

