**Example 1: 新建DSPA风险评估任务**

新创建dspa风险任务

Input: 

```
tccli dsgc CreateDSPAAssessmentTask --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --Name test \
    --BusinessName tx \
    --BusinessDept tx \
    --BusinessOwner tx \
    --TemplateId template-00000000 \
    --DiscoveryCondition.RDBInstances.0.DataSourceId cdb-5vskvzvn \
    --DiscoveryCondition.RDBInstances.0.DataSourceType cdb \
    --DiscoveryCondition.RDBInstances.0.ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "TaskId": "task-mdfmnme4",
        "RequestId": "9a9f5c32-95ab-4130-ae37-047cde38b943"
    }
}
```

