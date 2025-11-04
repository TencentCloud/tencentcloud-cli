**Example 1: 提交一个"hello world"作业任务**

提交一个"hello world"作业任务

Input: 

```
tccli thpc SubmitJob --cli-unfold-argument  \
    --ClusterId hpc-5fdafdsas \
    --Job.Tasks.0.Application.Commands.0.Command echo hello world \
    --Job.Tasks.0.Application.StorageMounts.0.Source /mnt/ \
    --Job.Tasks.0.Application.StorageMounts.0.Target /data/ \
    --Job.Tasks.0.Application.EnvVars.0.Name ENV \
    --Job.Tasks.0.Application.EnvVars.0.Value prod \
    --Job.Tasks.0.Application.Docker.Image test:test \
    --Job.Tasks.0.Application.Docker.RunArgs --privileged --cap-add=IPC_LOCK --net=host --ipc=host ' --gpus all' \
    --Job.Tasks.0.Application.OutputRedirect.Driver local \
    --Job.Tasks.0.Application.OutputRedirect.Options stdout=/data/${BATCH_JOB_ID}.log stderr=/data/${BATCH_JOB_ID}.log \
    --Job.Tasks.0.TaskName task-test-v1 \
    --Job.Tasks.0.TaskInstanceNum 2 \
    --Job.Tasks.0.Timeout 3600 \
    --Job.JobName hello world \
    --Job.JobDescription job test \
    --Job.Priority 1 \
    --QueueName compute
```

Output: 
```
{
    "Response": {
        "JobId": "job-mudfdafada",
        "RequestId": "ef8a9572-db7f-450b-b736-265feffafda34"
    }
}
```

