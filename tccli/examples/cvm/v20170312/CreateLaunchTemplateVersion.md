**Example 1: 创建实例启动模板新版本**

本示例使用最少的参数，基于默认启动模板版本号创建新的版本。这里将默认版本中的实例创建位置选择为广州一区

Input: 

```
tccli cvm CreateLaunchTemplateVersion --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-1 \
    --LaunchTemplateId lt-lobxe2yo
```

Output: 
```
{
    "Response": {
        "LaunchTemplateVersionNumber": 7,
        "RequestId": "9b4ad85f-1657-4445-111d-3c0a9fbec309"
    }
}
```

