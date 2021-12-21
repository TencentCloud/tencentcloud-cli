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
            {
                "LaunchTemplateVersion": 1,
                "LaunchTemplateVersionData": {},
                "CreationTime": "2020-12-17T01:54:31Z",
                "LaunchTemplateId": "lt-b8v1kcyq",
                "IsDefaultVersion": true,
                "LaunchTemplateVersionDescription": "",
                "CreatedBy": "251009920"
            }
        ],
        "RequestId": "b2da6ace-add1-48dc-ae73-6fc1eed95f1d"
    }
}
```

