**Example 1: 创建项目参数**

创建项目参数

Input: 

```
tccli wedata CreateProjectParamDs --cli-unfold-argument  \
    --Request.0.ParamKey abc \
    --Request.0.ParamType abc \
    --Request.0.ParamDefine abc \
    --Request.0.ProjectId abc \
    --Request.0.OperatorName abc \
    --Request.0.WorkflowId abc \
    --Request.0.SqlContent abc \
    --Request.0.CurRunDate abc \
    --Request.0.StartTime abc \
    --Request.0.TaskId abc \
    --Request.0.KeyWords abc \
    --Request.0.MyVersion 0 \
    --Request.0.Upstream True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

