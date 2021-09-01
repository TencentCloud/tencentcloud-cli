**Example 1: 运行作业示例**



Input: 

```
tccli oceanus RunJobs --cli-unfold-argument  \
    --RunJobDescriptions.0.RunType 0 \
    --RunJobDescriptions.0.JobConfigVersion 1 \
    --RunJobDescriptions.0.StartMode xx \
    --RunJobDescriptions.0.JobId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "18e0bde4-3922-42ca-8bfd-a36eaa035da4"
    }
}
```

