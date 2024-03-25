**Example 1: 范例**

修改任务信息
POST / HTTP/1.1
Host: wedata.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ModifyTaskInfo
<公共请求参数>

Input: 

```
tccli wedata ModifyTaskInfo --cli-unfold-argument  \
    --ProjectId abc \
    --TaskId abc \
    --DelayTime 0 \
    --StartupTime 0 \
    --SelfDepend 0 \
    --StartTime abc \
    --EndTime abc \
    --TaskAction abc \
    --CycleType 0 \
    --CycleStep 0 \
    --CrontabExpression abc \
    --ExecutionStartTime abc \
    --ExecutionEndTime abc \
    --TaskName abc \
    --RetryWait 0 \
    --TryLimit 0 \
    --Retriable 0 \
    --RunPriority 0 \
    --TaskExt.0.Key abc \
    --TaskExt.0.Value abc \
    --ResourceGroup abc \
    --YarnQueue abc \
    --BrokerIp abc \
    --InCharge abc \
    --Notes abc \
    --TaskParamInfos.0.ParamKey abc \
    --TaskParamInfos.0.ParamValue abc \
    --SourceServer abc \
    --TargetServer abc \
    --DependencyWorkflow abc \
    --DependencyConfigDTOs.0.ParentTask.TaskId abc \
    --DependencyConfigDTOs.0.ParentTask.VirtualTaskId abc \
    --DependencyConfigDTOs.0.ParentTask.VirtualFlag True \
    --DependencyConfigDTOs.0.ParentTask.TaskName abc \
    --DependencyConfigDTOs.0.ParentTask.WorkflowId abc \
    --DependencyConfigDTOs.0.ParentTask.RealWorkflowId abc \
    --DependencyConfigDTOs.0.ParentTask.CycleType 0 \
    --DependencyConfigDTOs.0.SonTask.TaskId abc \
    --DependencyConfigDTOs.0.SonTask.VirtualTaskId abc \
    --DependencyConfigDTOs.0.SonTask.VirtualFlag True \
    --DependencyConfigDTOs.0.SonTask.TaskName abc \
    --DependencyConfigDTOs.0.SonTask.WorkflowId abc \
    --DependencyConfigDTOs.0.SonTask.RealWorkflowId abc \
    --DependencyConfigDTOs.0.SonTask.CycleType 0 \
    --DependencyConfigDTOs.0.DependConfType abc \
    --DependencyConfigDTOs.0.SubordinateCyclicType abc \
    --DependencyConfigDTOs.0.DependencyStrategy abc \
    --ExecutionTTL 0 \
    --ScriptChange True
```

Output: 
```
{
    "Response": {
        "RequestId": "2e409eea-c8c8-4d3e-98b3-d8fdc960b631",
        "Data": true
    }
}
```

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata ModifyTaskInfo --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "11d5af39-eac3-4960-b0d5-5cced5cdc49f"
    }
}
```

