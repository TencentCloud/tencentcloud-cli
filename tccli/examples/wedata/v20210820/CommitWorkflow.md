**Example 1: 工作流版本提交**

工作流版本提交

Input: 

```
tccli wedata CommitWorkflow --cli-unfold-argument  \
    --ProjectId abc \
    --WorkflowId abc \
    --CommitDesc abc
```

Output: 
```
{
    "Response": {
        "ProjectId": "abc",
        "WorkflowId": "abc",
        "VersionNum": "abc",
        "VersionId": "abc",
        "RequestId": "abc"
    }
}
```

