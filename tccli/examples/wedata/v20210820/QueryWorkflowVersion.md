**Example 1: 查询工作流版本信息**

查询工作流版本信息

Input: 

```
tccli wedata QueryWorkflowVersion --cli-unfold-argument  \
    --ProjectId abc \
    --WorkflowId abc
```

Output: 
```
{
    "Response": {
        "ProjectId": "abc",
        "WorkflowId": "abc",
        "VersionInfos": [
            {
                "VersionNum": "abc",
                "VersionId": "abc",
                "Committer": "abc",
                "CommitTime": "abc",
                "CommitDesc": "abc",
                "CosUrl": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

