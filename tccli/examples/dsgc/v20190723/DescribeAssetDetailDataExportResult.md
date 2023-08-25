**Example 1: 查询敏感数据导出结果**

查询敏感数据导出结果URL

Input: 

```
tccli dsgc DescribeAssetDetailDataExportResult --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --ExportTaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "ExportResult": "Success",
        "ExportFileUrl": "https://datagov-test-cd-1258344699.cos.ap-chengdu.myqcloud.com/xxx.csv"
    }
}
```

