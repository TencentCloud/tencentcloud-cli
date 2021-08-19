**Example 1: DescribeImageTags**



Input: 

```
tccli tsf DescribeImageTags --cli-unfold-argument  \
    --TcrRepoInfo.RegistryName xx \
    --TcrRepoInfo.Namespace xx \
    --TcrRepoInfo.Region xx \
    --TcrRepoInfo.RegistryId xx \
    --TcrRepoInfo.RepoName xx \
    --QueryImageIdFlag 0 \
    --Limit 0 \
    --SearchWord xx \
    --Offset 0 \
    --RepoType xx \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "UpdateTime": "xx",
                    "DockerVersion": "xx",
                    "Author": "xx",
                    "TcrRepoInfo": {
                        "RegistryName": "xx",
                        "Namespace": "xx",
                        "Region": "xx",
                        "RegistryId": "xx",
                        "RepoName": "xx"
                    },
                    "TagId": "xx",
                    "CreationTime": "xx",
                    "RepoName": "xx",
                    "ImageId": "xx",
                    "SizeByte": 0,
                    "Architecture": "xx",
                    "TagName": "xx",
                    "PushTime": "xx",
                    "Os": "xx",
                    "Size": "xx"
                }
            ],
            "TotalCount": 0,
            "RepoName": "xx",
            "Server": "xx"
        },
        "RequestId": "xx"
    }
}
```

