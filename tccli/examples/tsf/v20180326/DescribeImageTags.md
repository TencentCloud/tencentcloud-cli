**Example 1: 镜像版本列表**



Input: 

```
tccli tsf DescribeImageTags --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100 \
    --ApplicationId application-xxxxxxx \
    --QueryImageIdFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "93445e4b-1d76-4cdb-95ed-1d0a4ed42171",
        "Result": {
            "Content": [
                {
                    "RepoName": "tsf_1000061xxxxx/test",
                    "TagName": "test",
                    "TagId": "sha256:6xxxxxxx4a5xxxxxxxb6fdxxxxxxx43dedxxxxxxx123xxxxxxxca83",
                    "ImageId": "sha256:f9bc8xxxxxxx1d591xxxxxxx70dc43xxxxxxxe00bef40a1762a",
                    "Size": "230 MB",
                    "CreationTime": "2019-05-23T05:51:19Z",
                    "UpdateTime": "2019-05-29T09:36:26Z",
                    "Author": "",
                    "Architecture": "amd64",
                    "DockerVersion": "18.09.0",
                    "Os": "linux",
                    "PushTime": "2019-05-29T09:36:22Z",
                    "SizeByte": 230967859
                }
            ],
            "TotalCount": 1,
            "Reponame": "tsf_10000617xxxx/test",
            "Server": "ccr.ccs.tencentyun.com"
        }
    }
}
```

