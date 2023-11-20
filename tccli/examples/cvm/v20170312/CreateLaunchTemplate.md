**Example 1: 使用最简单参数创建实例启动模板**

只传必传的Zone、镜像ID和启动模板ID，其他均采用系统默认值，具体配置如下：实例所在位置为广州二区，镜像ID为：img-pmqg1cw7，实例启动模板名称：test

Input: 

```
tccli cvm CreateLaunchTemplate --cli-unfold-argument  \
    --LaunchTemplateName test \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7
```

Output: 
```
{
    "Response": {
        "LaunchTemplateId": "lt-lobxe2yo",
        "RequestId": "9b4ad85f-1657-4445-111d-3c0a9fbec309"
    }
}
```

