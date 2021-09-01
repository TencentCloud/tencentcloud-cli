**Example 1: 创建任务流程示例**



Input: 

```
tccli emr RunJobFlow --cli-unfold-argument  \
    --Name test \
    --CreateCluster false \
    --InstancePolicy Terminate \
    --Steps.0.Name MRtest \
    --Steps.0.ExecutionStep.JobType MR \
    --Steps.0.ExecutionStep.Args /usr/local/service/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.5.jar wordcount cosn://testbucket/README.txt cosn://testbucket/output \
    --Steps.0.ActionOnFailure CONTINUE \
    --Steps.0.User hadoop
```

Output: 
```
{
    "Response": {
        "JobFlowId": 42,
        "RequestId": "ba25bfcf-86d6-451a-b01d-a28762c92b99"
    }
}
```

