**Example 1: 修改默认实例启动模板版本号**

本例将ID为lt-34vaef8fe的实例启动模板的默认启动版本号设置为2

Input: 

```
tccli cvm ModifyLaunchTemplateDefaultVersion --cli-unfold-argument  \
    --LaunchTemplateId lt-34vaef8fe \
    --DefaultVersion 2
```

Output: 
```
{
    "Response": {
        "RequestId": "9b4ad85f-1657-4445-111d-3c0a9fbec311"
    }
}
```

