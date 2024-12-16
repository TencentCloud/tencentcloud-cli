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
            "RepoName": "tsf_1382720xxxxx/nginx",
            "Server": "ccr.tencent.com",
            "Content": [
                {
                    "RepoName": "tsf_1382720xxxxx/nginx",
                    "TagName": "v1",
                    "TagId": "tag-6a79x94v",
                    "ImageId": "img-6a79x94v",
                    "Size": "256m",
                    "CreationTime": "2020-11-22 09:33:13",
                    "UpdateTime": "2020-11-23 09:33:13",
                    "Author": "user",
                    "Architecture": "x86",
                    "DockerVersion": "1.16",
                    "Os": "centos",
                    "PushTime": "2020-11-22 09:33:13",
                    "SizeByte": 0
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

