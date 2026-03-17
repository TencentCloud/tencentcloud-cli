**Example 1: 描述漏洞防御详情主机视角**



Input: 

```
tccli cwp DescribeRaspEventDetailCWP --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "资源不存在"
        },
        "RequestId": "80d680af-f02c-4a38-9ab9-e6dad641cfca"
    }
}
```

