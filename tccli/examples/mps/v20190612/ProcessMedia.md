**Example 1: Initiating a transcoding task**

This example shows you how to initiate a transcoding task for a video at a specified COS endpoint to output in three formats of 20, 30, and 40.

Input: 

```
tccli mps ProcessMedia --cli-unfold-argument  \
    --InputInfo.Type COS\
    --InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88\
    --InputInfo.CosInputInfo.Region ap-chongqing\
    --InputInfo.CosInputInfo.Object /movie/201907/WildAnimal.mov\
    --MediaProcessTask.TranscodeTaskSet.0.Definition 20\
    --MediaProcessTask.TranscodeTaskSet.1.Definition 30\
    --MediaProcessTask.TranscodeTaskSet.2.Definition 40
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

