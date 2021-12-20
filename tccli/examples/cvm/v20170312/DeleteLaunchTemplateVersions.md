**Example 1: 删除实例启动模板版本**

本例删除启动模板lt-34vaef8fe中的版本号为2和3版本

Input: 

```
tccli cvm DeleteLaunchTemplateVersions --cli-unfold-argument  \
    --LaunchTemplateId lt-34vaef8fe \
    --LaunchTemplateVersions 2 3
```

Output: 
```
{
    "Response": {
        "RequestId": "9b4ad85f-1657-4445-111d-3c0a9fbec311"
    }
}
```

