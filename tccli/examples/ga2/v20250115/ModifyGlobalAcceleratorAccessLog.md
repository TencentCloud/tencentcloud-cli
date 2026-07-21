**Example 1: 修改访问日志示例**



Input: 

```
tccli ga2 ModifyGlobalAcceleratorAccessLog --cli-unfold-argument  \
    --LogPushTaskId galog-5nz8egdx \
    --GlobalAcceleratorId ga-8sreohed \
    --CloudLogId ce5aa025-1c29-4d8b-8f84-d960e22acb3f \
    --CloudLogSetId 81217ea2-f578-451a-946e-f31e2131a9ac \
    --FieldKeys session_time \
    --FlowLogDescription ****-测试创建日志任务-修改
```

Output: 
```
{
    "Response": {
        "RequestId": "8785e7bc-a0d0-4dff-ac0b-f56152969ed9"
    }
}
```

