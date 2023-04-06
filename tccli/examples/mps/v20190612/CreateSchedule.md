**Example 1: 设置转码规则**

对名为 evan-test-1300828900 的Bucket 创建编排，当 mp4或者flv文件上传到 /input/ 目录时，触发多次转码任务，转码模板ID为 10。

Input: 

```
tccli mps CreateSchedule --cli-unfold-argument  \
    --ScheduleName evan_test7 \
    --Trigger.Type CosFileUpload \
    --Trigger.CosFileUploadTrigger.Bucket evan-test-1300828900 \
    --Trigger.CosFileUploadTrigger.Region ap-guangzhou \
    --Trigger.CosFileUploadTrigger.Dir /input/ \
    --Trigger.CosFileUploadTrigger.Formats mp4 flv \
    --Activities.0.ActivityType input \
    --Activities.0.ReardriveIndex 1 2 \
    --Activities.1.ActivityType action-trans \
    --Activities.1.ReardriveIndex 3 \
    --Activities.1.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.2.ActivityType action-trans \
    --Activities.2.ReardriveIndex 6 7 \
    --Activities.2.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.3.ActivityType action-trans \
    --Activities.3.ReardriveIndex 4 5 \
    --Activities.3.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.4.ActivityType action-trans \
    --Activities.4.ReardriveIndex 10 \
    --Activities.4.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.5.ActivityType action-trans \
    --Activities.5.ReardriveIndex 10 \
    --Activities.5.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.6.ActivityType action-trans \
    --Activities.6.ReardriveIndex 10 \
    --Activities.6.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.7.ActivityType action-trans \
    --Activities.7.ReardriveIndex 8 \
    --Activities.7.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.8.ActivityType action-trans \
    --Activities.8.ReardriveIndex 9 \
    --Activities.8.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.9.ActivityType action-trans \
    --Activities.9.ReardriveIndex 10 \
    --Activities.9.ActivityPara.TranscodeTask.Definition 10 \
    --Activities.10.ActivityType output \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket evan-test-1300828900 \
    --OutputStorage.CosOutputStorage.Region ap-nanjing \
    --OutputDir output/
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "ScheduleId": 157482
    }
}
```

