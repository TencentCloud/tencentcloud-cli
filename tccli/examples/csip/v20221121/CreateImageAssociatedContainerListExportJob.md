**Example 1: 创建镜像关联容器资产导出任务**



Input: 

```
tccli csip CreateImageAssociatedContainerListExportJob --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 30 \
    --Save 1 \
    --ExportName container_list
```

Output: 
```
{
    "Response": {
        "JobID": "3af9e46b-2be3-40a3-90eb-6621619ab965",
        "RequestId": "9d379630-c358-4453-8086-162e6a558c2a"
    }
}
```

