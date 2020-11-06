**Example 1: 更改任务模板**



Input: 

```
tccli batch ModifyTaskTemplate --cli-unfold-argument  \
    --TaskTemplateId task-tmpl-606i415o \
    --TaskTemplateName A \
    --TaskTemplateDescription test \
    --TaskTemplateInfo.TaskName A \
    --TaskTemplateInfo.TaskInstanceNum 1 \
    --TaskTemplateInfo.Application.DeliveryForm LOCAL \
    --TaskTemplateInfo.Application.Command 'python -c "fib' \
    --TaskTemplateInfo.ComputeEnv.EnvType MANAGED \
    --TaskTemplateInfo.ComputeEnv.EnvData.InstanceType S1.SMALL1 \
    --TaskTemplateInfo.ComputeEnv.EnvData.ImageId img-bd78fy2t \
    --TaskTemplateInfo.RedirectInfo.StdoutRedirectPath cos://bucket-appid.cos.ap-guangzhou.myqcloud.com/hello2/logs/ \
    --TaskTemplateInfo.RedirectInfo.StderrRedirectPath cos://bucket-appid.ap-guangzhou.myqcloud.com/hello2/logs/
```

Output: 
```
{
    "Response": {
        "RequestId": "8a56bd93-688e-41c3-bc8b-f9867ffb0dd0"
    }
}
```

