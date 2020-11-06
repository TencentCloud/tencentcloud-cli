**Example 1: 创建任务模板**



Input: 

```
tccli batch CreateTaskTemplate --cli-unfold-argument  \
    --TaskTemplateName A \
    --TaskTemplateDescription test \
    --TaskTemplateInfo.TaskName A \
    --TaskTemplateInfo.TaskInstanceNum 1 \
    --TaskTemplateInfo.Application.DeliveryForm LOCAL \
    --TaskTemplateInfo.Application.Command python-c"fib \
    --TaskTemplateInfo.ComputeEnv.EnvType MANAGED \
    --TaskTemplateInfo.ComputeEnv.EnvData.InstanceType S1.SMALL1 \
    --TaskTemplateInfo.ComputeEnv.EnvData.ImageId img-bd78fy2t \
    --TaskTemplateInfo.RedirectInfo.StdoutRedirectPath cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/ \
    --TaskTemplateInfo.RedirectInfo.StderrRedirectPath cos://bucket-appid.cosgz.myqcloud.com/hello2/logs/
```

Output: 
```
{
    "Response": {
        "TaskTemplateId": "task-tmpl-7vtx96n2",
        "RequestId": "83cd875b-7ac0-4e5b-b150-0e69c59e5e52"
    }
}
```

