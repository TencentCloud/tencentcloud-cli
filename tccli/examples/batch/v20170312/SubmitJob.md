**Example 1: 提交作业**



Input: 

```
tccli batch SubmitJob --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --Job.JobName test \
    --Job.JobDescription test \
    --Job.Priority 1 \
    --Job.Tasks.0.TaskName hello2 \
    --Job.Tasks.0.TaskInstanceNum 1 \
    --Job.Tasks.0.Application.DeliveryForm LOCAL \
    --Job.Tasks.0.Application.Command 'python -c "fib' \
    --Job.Tasks.0.ComputeEnv.EnvType MANAGED \
    --Job.Tasks.0.ComputeEnv.EnvData.InstanceType S1.SMALL1 \
    --Job.Tasks.0.ComputeEnv.EnvData.ImageId img-bd78fy2t \
    --Job.Tasks.0.RedirectInfo.StdoutRedirectPath cos://dondonbatch-1251783334.cosgz.myqcloud.com/hello2/logs/ \
    --Job.Tasks.0.RedirectInfo.StderrRedirectPath cos://dondonbatch-1251783334.cosgz.myqcloud.com/hello2/logs/
```

Output: 
```
{
    "Response": {
        "JobId": "job-4yn0we13",
        "RequestId": "bf2a9734-e485-423f-9d73-a93f5e6c6a0c"
    }
}
```

**Example 2: 提交DAG型作业，具有依赖关系**



Input: 

```
tccli batch SubmitJob --cli-unfold-argument  \
    --Placement.Zone ap-beijing-2 \
    --Job.JobName dag \
    --Job.JobDescription dag_demo \
    --Job.Tasks.0.TaskName pre_task \
    --Job.Tasks.0.TaskInstanceNum 1 \
    --Job.Tasks.0.Application.DeliveryForm LOCAL \
    --Job.Tasks.0.Application.Command 'echo pre_task' \
    --Job.Tasks.0.ComputeEnv.EnvData.InstanceType S2.SMALL1 \
    --Job.Tasks.0.RedirectInfo.StdoutRedirectPath cos://batch-demo-1251783334.cosbj.myqcloud.com/logs/ \
    --Job.Tasks.0.RedirectInfo.StderrRedirectPath cos://batch-demo-1251783334.cosbj.myqcloud.com/logs/ \
    --Job.Tasks.1.TaskName post_task \
    --Job.Tasks.1.TaskInstanceNum 1 \
    --Job.Tasks.1.Application.DeliveryForm LOCAL \
    --Job.Tasks.1.Application.Command 'echo post_task' \
    --Job.Tasks.1.ComputeEnv.EnvData.InstanceType S2.SMALL1 \
    --Job.Tasks.1.RedirectInfo.StdoutRedirectPath cos://batch-demo-1251783334.cosbj.myqcloud.com/logs/ \
    --Job.Tasks.1.RedirectInfo.StderrRedirectPath cos://batch-demo-1251783334.cosbj.myqcloud.com/logs/ \
    --Job.Dependences.0.StartTask pre_task \
    --Job.Dependences.0.EndTask post_task
```

Output: 
```
{
    "Response": {
        "JobId": "job-2bmv4p7o",
        "RequestId": "165dc518-52a4-4363-8ea4-14f1ee8dea1a"
    }
}
```

