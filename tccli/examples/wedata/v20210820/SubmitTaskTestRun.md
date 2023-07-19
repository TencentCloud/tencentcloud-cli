**Example 1: 编排空间试运行**

编排空间试运行

Input: 

```
tccli wedata SubmitTaskTestRun --cli-unfold-argument  \
    --WorkFlowId abc \
    --Name abc \
    --Tasks.0.ClusterId abc \
    --Tasks.0.StageId abc \
    --Tasks.0.JobId abc \
    --Tasks.0.StageName abc \
    --Tasks.0.Type abc \
    --Tasks.0.Mode abc \
    --Tasks.0.Version abc \
    --Tasks.0.Queue abc \
    --Tasks.0.Content abc \
    --Tasks.0.Parameters.0.Key abc \
    --Tasks.0.Parameters.0.Value abc \
    --Tasks.0.Description abc \
    --Tasks.0.ProjectId abc \
    --Tasks.0.JobType abc \
    --Tasks.0.WorkFlowId abc \
    --Description abc \
    --TaskIds abc \
    --ProjectId abc \
    --RunParams abc \
    --ScriptContent abc \
    --VersionId abc
```

Output: 
```
{
    "Response": {
        "JobId": 0,
        "RecordId": [
            0
        ],
        "RequestId": "abc"
    }
}
```

