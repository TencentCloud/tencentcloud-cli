**Example 1: success**



Input: 

```
tccli tcbr DeleteCloudRunServer --cli-unfold-argument  \
    --ServerName 字符串 \
    --EnvId 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "dbbbff45-c033-4b5b-8ccf-92ba6041be99",
        "Result": ""
    }
}
```

**Example 2: success-1**



Input: 

```
tccli tcbr DeleteCloudRunServer --cli-unfold-argument  \
    --ServerName 字符串 \
    --EnvId 字符串 \
    --OperatorRemark 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "0db47e7b-3330-4ea7-bcde-7bd5e2bada7f",
        "Result": "succ"
    }
}
```

**Example 3: DeleteCloudRunServer**

删除服务

Input: 

```
tccli tcbr DeleteCloudRunServer --cli-unfold-argument  \
    --EnvId envId \
    --ServerName serverName
```

Output: 
```
{
    "Response": {
        "Result": "success",
        "RequestId": "57832ae4-e87d-4b85-aa6e-97b673aa994f"
    }
}
```

