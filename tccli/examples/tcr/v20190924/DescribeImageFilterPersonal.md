**Example 1: 查询个人版与指定tag镜像内容相同的tag列表**



Input: 

```
tccli tcr DescribeImageFilterPersonal --cli-unfold-argument  \
    --RepoName dockerhub/test \
    --Tag test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "SameImages": [
                "99"
            ]
        }
    }
}
```

