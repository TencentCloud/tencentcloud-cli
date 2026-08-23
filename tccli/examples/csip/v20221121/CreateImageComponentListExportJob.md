**Example 1: 创建镜像组件列表导出任务**



Input: 

```
tccli csip CreateImageComponentListExportJob --cli-unfold-argument  \
    --Id 20 \
    --MemberId mem-12e1se11 \
    --Save 1 \
    --ExportName component_list
```

Output: 
```
{
    "Response": {
        "JobID": "efcd0b16-b60e-4b8d-ac8d-045f2a0c9cdd",
        "RequestId": "d257f5f4-5fa2-4863-89ae-6f8c99775a36"
    }
}
```

