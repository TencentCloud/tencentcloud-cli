**Example 1: 查询本地镜像组件列表**



Input: 

```
tccli tcss DescribeImageComponentList --cli-unfold-argument  \
    --ImageID image-id \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "ImageID": "sha256:2ebe27d",
                "Name": "name",
                "Path": "Path",
                "Type": "SYSTEM_COMPONENT",
                "Version": "2.2.51-12.el7",
                "VulCount": 0
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

