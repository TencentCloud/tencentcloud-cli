**Example 1: 获取共享版镜像仓库tag列表**



Input: 

```
tccli tcr DescribeImagePersonal --cli-unfold-argument  \
    --RepoName dockerhub/test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "RepoName": "dockerhub/test",
            "Server": "ccr.ccs.tencentyun.com",
            "TagCount": 1,
            "TagInfo": [
                {
                    "Id": 2089896,
                    "TagName": "latest",
                    "TagId": "sha256:ad207667c53d9739f1f6c2d0f9eedf5237c969e7d11ef4bd3f4b23b68b5eac6c",
                    "ImageId": "sha256:db8493d07bbb3b91e989466825393fedd910d695ac6671ec7fc4ab636cf1aafd",
                    "Size": "128 MB",
                    "CreationTime": "2019-10-17 15:59:30 +0800 CST",
                    "DurationDays": "",
                    "Author": "",
                    "Architecture": "amd64",
                    "DockerVersion": "19.03.1",
                    "OS": "linux",
                    "UpdateTime": "2019-10-24 14:20:55 +0800 CST",
                    "PushTime": "2019-10-24 14:20:51 +0800 CST",
                    "SizeByte": 128152591
                }
            ]
        }
    }
}
```

