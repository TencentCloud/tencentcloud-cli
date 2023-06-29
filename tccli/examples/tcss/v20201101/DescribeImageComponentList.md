**Example 1: 查询本地镜像组件列表**



Input: 

```
tccli tcss DescribeImageComponentList --cli-unfold-argument  \
    --ImageID xx \
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
                "Name": "xx",
                "ImageID": "xx",
                "Version": "xx",
                "VulCount": 1,
                "Path": "xx",
                "Type": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

