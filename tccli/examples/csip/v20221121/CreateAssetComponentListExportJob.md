**Example 1: 创建镜像资产中组件列表导出任务**



Input: 

```
tccli csip CreateAssetComponentListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName asset_component
```

Output: 
```
{
    "Response": {
        "JobID": "a9e94405-5853-403e-9431-00c2ea9339e2",
        "RequestId": "4878a387-f2fc-455a-b0d7-0f4ab2130e40"
    }
}
```

