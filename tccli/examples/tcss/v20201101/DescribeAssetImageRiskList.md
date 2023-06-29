**Example 1: 查询镜像风险列表**

查询镜像风险列表

Input: 

```
tccli tcss DescribeAssetImageRiskList --cli-unfold-argument  \
    --ImageID dskaldjskld
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Behavior": 3,
                "Level": 3,
                "Type": 2,
                "Desc": "Dockerfile中存在账号密码、认证凭据等敏感信息",
                "InstructionContent": "/bin/sh -c #(nop)  ENV PWD=postgresql://1.1.1.1:xxx@yyy"
            },
            {
                "Behavior": 3,
                "Level": 3,
                "Type": 2,
                "Desc": "Dockerfile中存在账号密码、认证凭据等敏感信息",
                "InstructionContent": "/bin/sh -c echo root:654321 | chpasswd"
            }
        ],
        "RequestId": "ff49ad4b-fe52-4f9d-8810-ba377eab9124",
        "TotalCount": 6
    }
}
```

