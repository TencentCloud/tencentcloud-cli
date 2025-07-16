**Example 1: 修改编排**

修改编排

Input: 

```
tccli mps ModifySchedule --cli-unfold-argument  \
    --ScheduleId 22435 \
    --Trigger.Type AwsS3FileUpload \
    --Trigger.AwsS3FileUploadTrigger.S3Bucket evanxia-test \
    --Trigger.AwsS3FileUploadTrigger.S3Region us-east-1 \
    --Trigger.AwsS3FileUploadTrigger.Dir /input/
```

Output: 
```
{
    "Response": {
        "RequestId": "974e52bf-1234-49bf-8bcd-fdeca9b2d290"
    }
}
```

