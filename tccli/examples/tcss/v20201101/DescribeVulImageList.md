**Example 1: 查询漏洞影响的镜像列表**



Input: 

```
tccli tcss DescribeVulImageList --cli-unfold-argument  \
    --PocID 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "ComponentList": [
                    {
                        "Path": "xx",
                        "Version": "xx",
                        "Name": "xx",
                        "FixedVersion": "xx"
                    }
                ],
                "HostCount": 0,
                "ImageName": "xx",
                "ContainerCount": 0,
                "ImageID": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

