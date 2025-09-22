**Example 1: 获取任务实例的日志**

包含日志和对应执行代码

Input: 

```
tccli wedata GetTaskInstanceLog --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --InstanceKey 20250619121143818_2025-08-28 12:55:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeContent": "set tez.queue.name=default;<br>set mapreduce.job.queuename=default;<br>set tez.job.name=job_20250619121143818_20250828125500;<br>set mapred.job.name=job_20250619121143818_20250828125500;<br>show tables;",
            "InstanceKey": "20250619121143818_2025-08-28 12:55:00",
            "LogInfo": "2025-08-28 15:04:17 DEBUG the customize_settings file exists in /data/execute_worker/conf/runner_customize.properties<br>2025-08-28 15:04:17 DEBUG runner.language:null<br>2025-08-28 15:04:17 DEBUG init messageSource<br>2025-08-28 15:04:17 DEBUG load guldan_runner_messages<br>2025-08-28 15:04:17 INFO 第1步, 开始执行",
            "NextCursor": "26783",
            "ProjectId": "2428908825624145920"
        },
        "RequestId": "54a7181f-7ab6-4f8e-a630-d1cbe88f2230"
    }
}
```

