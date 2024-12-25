**Example 1: DescribeImageTags**



Input: 

```
tccli tsf DescribeImageTags --cli-unfold-argument  \
    --ApplicationId application-yx8kjmra \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "4df95eea-e433-41c6-9c65-cfd1bd05d5d0",
        "Result": {
            "Content": [
                {
                    "Architecture": "amd64",
                    "Author": "",
                    "CreationTime": "2024-12-17T11:55:49Z",
                    "DockerVersion": "",
                    "ImageId": "sha256:b774178107747295705e9f919e5cf009d2dad7f343f18dea74a9f3b13e03b6ec",
                    "Os": null,
                    "PushTime": "2024-12-17T11:55:49Z",
                    "RepoName": "tsf_100011913960/mesh-no-spec",
                    "Size": "72 MB",
                    "SizeByte": 72225778,
                    "TagId": "sha256:4c270bbe6abe54d0b9c5186d5c2d79a32b932fc65f5628518b88c093f69ecc19",
                    "TagName": "1217",
                    "TcrRepoInfo": null,
                    "UpdateTime": "2024-12-17T11:55:57Z"
                }
            ],
            "RepoName": "tsf_100011913960/mesh-no-spec",
            "Server": "ccr.ccs.tencentyun.com",
            "TotalCount": 1
        }
    }
}
```

