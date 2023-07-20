**Example 1: 查询工作流任务数**

查询工作流任务数

Input: 

```
tccli wedata DescribeWorkflowTaskCount --cli-unfold-argument  \
    --WorkflowId abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1,
            "TypeCount": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "CycleCount": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

