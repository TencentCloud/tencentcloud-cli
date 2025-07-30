**Example 1: 例子**



Input: 

```
tccli wedata DescribeSuccessorTaskInfoList --cli-unfold-argument  \
    --TaskIds abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "abc",
                "WorkflowId": "abc",
                "TaskName": "abc",
                "Layer": 0,
                "Status": "abc",
                "TaskTypeId": 0,
                "InCharge": "abc",
                "ProjectId": "abc",
                "ProjectName": "abc",
                "WorkflowName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

