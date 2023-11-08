**Example 1: DescribeImageTags**



Input: 

```
tccli tsf DescribeImageTags --cli-unfold-argument  \
    --ApplicationId abc \
    --Offset 0 \
    --Limit 20 \
    --QueryImageIdFlag 0 \
    --SearchWord abc \
    --RepoType abc \
    --RepoName abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "RepoName": "abc",
            "Server": "abc",
            "Content": [
                {
                    "RepoName": "abc",
                    "TagName": "abc",
                    "TagId": "abc",
                    "ImageId": "abc",
                    "Size": "abc",
                    "CreationTime": "abc",
                    "UpdateTime": "abc",
                    "Author": "abc",
                    "Architecture": "abc",
                    "DockerVersion": "abc",
                    "Os": "abc",
                    "PushTime": "abc",
                    "SizeByte": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

