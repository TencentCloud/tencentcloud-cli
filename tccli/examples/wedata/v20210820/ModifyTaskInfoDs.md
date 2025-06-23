**Example 1: 成功示例**

成功示例

Input: 

```
tccli wedata ModifyTaskInfoDs --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --TaskId 20241230120158580 \
    --DelayTime 240 \
    --StartupTime 0 \
    --StartTime 2025-02-13 00:00:00 \
    --EndTime 2100-01-01 23:59:59 \
    --TaskAction  \
    --CycleType 2 \
    --CycleStep 1 \
    --ExecutionStartTime 04:00 \
    --ExecutionEndTime 03:59 \
    --TaskName 1230_test \
    --RetryWait 5 \
    --TryLimit 5 \
    --Retriable 1 \
    --RunPriority 6 \
    --TaskExt.0.Key bucket \
    --TaskExt.0.Value wedata-fusion-dev-1257305158 \
    --TaskExt.1.Key calendar_id \
    --TaskExt.1.Value  \
    --TaskExt.2.Key ftp.file.name \
    --TaskExt.2.Value https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com/datastudio/project/1464962169590902784/默认文件夹/peanut/test_delete_3/1230_test.sh \
    --TaskExt.3.Key tenantId \
    --TaskExt.3.Value 1257305158 \
    --TaskExt.4.Key calendar_open \
    --TaskExt.4.Value 0 \
    --TaskExt.5.Key calendar_name \
    --TaskExt.5.Value  \
    --TaskExt.6.Key region \
    --TaskExt.6.Value ap-nanjing \
    --TaskExt.7.Key extraInfo \
    --TaskExt.7.Value &&&"fromMapping":false} \
    --TaskExt.8.Key data_cluster \
    --TaskExt.8.Value  \
    --TaskExt.9.Key enableKerberosLogin \
    --TaskExt.9.Value false \
    --TaskExt.10.Key waitExecutionTotalTTL \
    --TaskExt.10.Value -1 \
    --TaskExt.11.Key python_type \
    --TaskExt.11.Value python3 \
    --TaskExt.12.Key python_sub_version \
    --TaskExt.12.Value python3 \
    --ResourceGroup 20240703113703331017 \
    --BrokerIp any \
    --InCharge peanutzhu \
    --Notes  \
    --TaskParamInfos.0.ParamKey value1 \
    --TaskParamInfos.0.ParamValue test \
    --ExecutionTTL -1 \
    --ScriptChange False \
    --ScheduleTimeZone UTC+8 \
    --ScheduleRunType 0 \
    --RegisterDsEventPublisherRequest.ProjectId 1464962169590902784 \
    --RegisterDsEventPublisherRequest.Key 20241230120158580 \
    --RegisterDsEventPublisherRequest.Type REST_API \
    --RegisterDsEventPublisherRequest.Properties.0.ParamKey eventVariable \
    --RegisterDsEventPublisherRequest.Properties.0.ParamValue events \
    --RegisterDsEventPublisherRequest.Description  \
    --DependencyConfigDTOs.0.ParentTask.TaskId 20250606112604725 \
    --DependencyConfigDTOs.0.DependConfType MONTH \
    --DependencyConfigDTOs.0.SubordinateCyclicType CURRENT_MONTH \
    --DependencyConfigDTOs.0.DependencyStrategy EXECUTING
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "b41c3c3b-f7a8-4789-89f2-6b90711a6e5c"
    }
}
```

