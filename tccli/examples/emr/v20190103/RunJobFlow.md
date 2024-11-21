**Example 1: 创建任务流程示例**



Input: 

```
tccli emr RunJobFlow --cli-unfold-argument  \
    --Name pop-api-tmp-emr-phs-drug-monitor-daily--20241106115143 \
    --CreateCluster False \
    --Steps.0.Name DrugChangeRemindJob_20241106035136 \
    --Steps.0.ExecutionStep.JobType SPARK \
    --Steps.0.ExecutionStep.Args --master yarn --deploy-mode cluster --class com.patsnap.app.monitor.job.DrugChangeRemindJob --conf spark.driver.extraJavaOptions=-Dfile.encoding=utf-8 --conf spark.executor.extraJavaOptions=-Dfile.encoding=utf-8 cosn://data-phs-common-dataprod-ash-125000000/spark-jars/drug/drug_change_monitor/v1.0/data-phs-etl-app.jar ${program_config} \
    --Steps.0.ActionOnFailure CONTINUE \
    --Steps.0.User hadoop \
    --InstancePolicy Reserve \
    --InstanceId emr-64e
```

Output: 
```
{
    "Response": {
        "JobFlowId": 16531,
        "RequestId": "3f63c907-d4e4-4856-b05d-949eedc2151a"
    }
}
```

