**Example 1: 创建镜像扫描任务**



Input: 

```
tccli csip CreateImageRegistryScanTask --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --ScanType VUL \
    --Timeout 3600 \
    --Name 手动测试 \
    --Target.Mode ALL \
    --Target.ExcludeImages 784 \
    --Target.Images 790 \
    --Filter.RegistryType ccr \
    --Filter.Namespace openclaw
```

Output: 
```
{
    "Response": {
        "RequestId": "2c7728fc-49ef-4438-bf18-b55493421991"
    }
}
```

