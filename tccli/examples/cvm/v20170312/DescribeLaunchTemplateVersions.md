**Example 1: 查询实例模板版本信息**



Input: 

```
tccli cvm DescribeLaunchTemplateVersions --cli-unfold-argument  \
    --LaunchTemplateId lt-b8v1kcyq
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LaunchTemplateVersionSet": [
            {}
        ],
        "RequestId": "b2da6ace-add1-48dc-ae73-6fc1eed95f1d"
    }
}
```

