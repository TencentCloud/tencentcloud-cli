**Example 1: 查询实例启动模板**



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
            {}
        ],
        "RequestId": "b2d70642-c69a-4115-ae4e-f6ddade68fea"
    }
}
```

