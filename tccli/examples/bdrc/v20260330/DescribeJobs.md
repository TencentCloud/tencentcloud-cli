**Example 1: 查询agent任务**



Input: 

```
tccli bdrc DescribeJobs --cli-unfold-argument  \
    --JobIDs j-20260609033851-046bf895
```

Output: 
```
{
    "Response": {
        "JobExecuteInfo": [
            {
                "JobID": "j-20260609033851-046bf895",
                "JobInfo": "{\"JobID\": \"fb-iqspk0ma\", \"JobType\": \"BackUp\", \"CosURL\": \"s3:http://cos.ap-guangzhou.myqcloud.com/vault-j7ciunjt-gz-260094408/ins-fcs3wf2c\", \"RoleAK\": \"AKIDwsrka***rx5JOOH2ggW\", \"RoleSK\": \"pU0P***0BFPVS\", \"BrcRunnerPassword\": \"2aY**AMUQu7\", \"BackUpPath\": \"/mnt_vdb\", \"Exclude\": \"/proc,/sys,/dev,/run,/tmp,/snap,/lost+found,/media\", \"IncludeSuffixes\": \"\", \"IInclude\": \"\", \"BrcRunnerOptions\": \"s3.bucket-lookup=dns\", \"SubFolder\": \"\", \"OneFileSystem\": false, \"LimitUpload\": 0, \"LimitDownload\": 0}",
                "JobProgress": 100,
                "JobStatus": "SUCCESS",
                "JobType": "BACKUP"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ec3e013e-c4c2-4232-8f99-2564b7077947"
    }
}
```

