**Example 1: 提交sql任务**

提交sql任务

Input: 

```
tccli wedata SubmitJob --cli-unfold-argument  \
    --Job.JobType SQL \
    --Job.JobSource MANUAL_SCHEDULE \
    --Job.Name 查询历史数据任务 \
    --Job.Desc 从 tsing_catalog.xzp1.xzp_tb2.full_history 表获取历史数据 \
    --Job.WorkspaceId 17678671667189298 \
    --Job.AppId 260073493 \
    --Job.OwnerUin 700002164619 \
    --Job.ExecUin 700002164619 \
    --Job.ExecuteParam.TemplateInfo.Source 2 \
    --Job.ExecuteParam.TemplateInfo.ExecuteTemplate.Sql.Source 2 \
    --Job.ExecuteParam.TemplateInfo.ExecuteTemplate.Sql.Content SELECT * FROM tsing_catalog.xzp1.xzp_tb2.full_history LIMIT 100; \
    --Job.ExecuteParam.TemplateInfo.ExecuteTemplate.Sql.Catalog tsing_catalog \
    --Job.ExecuteParam.TemplateInfo.ExecuteTemplate.Sql.Schema xzp1 \
    --Job.ExecuteParam.TemplateInfo.ExecuteTemplate.TemplateType SQL \
    --Job.ExecuteParam.ComputeResource res-c07a503e
```

Output: 
```
{
    "Response": {
        "Data": {
            "HasSubmitBefore": false,
            "JobId": "6820260206163255029",
            "QuotaExceeded": false
        },
        "RequestId": "7ce85c02-f05d-4b8b-939a-816362f832ac"
    }
}
```

