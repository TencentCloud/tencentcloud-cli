**Example 1: 查询个人版与指定tag镜像内容相同的tag列表**



Input: 

```
tccli tcr DescribeImageFilterPersonal --cli-unfold-argument  \
    --RepoName nicokang/golang \
    --Tag 4
```

Output: 
```
{
    "Response": {
        "Data": {
            "SameImages": [
                "3"
            ]
        },
        "RequestId": "9b054042-5447-4902-bd48-2c92f5be5b0f"
    }
}
```

