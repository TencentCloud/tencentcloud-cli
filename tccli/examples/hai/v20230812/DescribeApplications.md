**Example 1: 查询应用**

查询应用

Input: 

```
tccli hai DescribeApplications --cli-unfold-argument  \
    --ApplicationIds app-jxnaqazx \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ApplicationSet": [
            {
                "ApplicationId": "app-jxnaqazx",
                "ApplicationName": "应用名称",
                "Description": "应用描述",
                "ConfigEnvironment": "Ubuntu20.04, Python 3.8, ChatGLM2-6b, CUDA 11.7, cuDNN 8, pytorch 2, JupyteLab",
                "MinSystemDiskSize": 80
            }
        ],
        "RequestId": "2b1fae52-8004-4a13-a20a-26ea1149f9df",
        "TotalCount": 1
    }
}
```

