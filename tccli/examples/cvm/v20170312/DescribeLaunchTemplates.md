**Example 1: 查询实例启动模板**

查询实例启动模板

Input: 

```
tccli cvm DescribeLaunchTemplates --cli-unfold-argument  \
    --LaunchTemplateIds lt-q9t8j8eg
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LaunchTemplateSet": [
            {
                "LatestVersionNumber": 12,
                "LaunchTemplateId": "lt-q9t8j8eg",
                "LaunchTemplateName": "未命名foo\"'\"'''\"\"",
                "DefaultVersionNumber": 5,
                "LaunchTemplateVersionCount": 8,
                "CreatedBy": "251009920",
                "CreationTime": "2020-12-16T08:05:02Z"
            }
        ],
        "RequestId": "b2d70642-c69a-4115-ae4e-f6ddade68fea"
    }
}
```

