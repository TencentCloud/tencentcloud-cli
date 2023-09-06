**Example 1: 添加查询应用启动路径列表请求**



Input: 

```
tccli car DescribeApplicationPathList --cli-unfold-argument  \
    --ApplicationId app-afdxfafc \
    --ApplicationVersionId ver-geyacbf
```

Output: 
```
{
    "Response": {
        "PathList": [
            "xxxx\\xxx.exe"
        ],
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

