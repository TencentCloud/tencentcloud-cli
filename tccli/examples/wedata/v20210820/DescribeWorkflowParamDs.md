**Example 1: 查询工作流全局参数**

查询工作流全局参数


Input: 

```
tccli wedata DescribeWorkflowParamDs --cli-unfold-argument  \
    --WorkflowId abc \
    --CurRunDate abc \
    --ProjectId 123123 \
    --StartTime abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 0,
                "ParamKey": "abc",
                "ParamType": "abc",
                "ParamBelong": "abc",
                "ParamDefine": "abc",
                "ParamValue": "abc",
                "ParamOwner": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Result": true,
                "Msg": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

