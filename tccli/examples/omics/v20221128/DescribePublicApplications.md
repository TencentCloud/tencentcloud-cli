**Example 1: 查询公共应用列表**

查询公共应用列表。

Input: 

```
tccli omics DescribePublicApplications --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Applications": [
            {
                "AppGroupType": "APP_COLLECTION",
                "AppId": "c798f9c0-cd28-446c-b8e4-3ec30ec1a7ff",
                "AppTags": [
                    {
                        "TagId": "3e497318-03ef-4483-838b-5c592d78d362",
                        "TagName": "AI 模型"
                    }
                ],
                "ApplicationId": "publicapp-nf-ori-collection",
                "Name": "ORI Collection (Nextflow)",
                "NextflowVersion": [],
                "Type": "NEXTFLOW"
            }
        ],
        "TotalCount": 19,
        "RequestId": "68c85386-9cd7-4761-a664-7b0f522fabae"
    }
}
```

