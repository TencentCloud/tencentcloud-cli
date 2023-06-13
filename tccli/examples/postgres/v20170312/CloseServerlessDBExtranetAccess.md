**Example 1: 关闭serverless公网地址**

关闭serverless公网地址

Input: 

```
tccli postgres CloseServerlessDBExtranetAccess --cli-unfold-argument  \
    --DBInstanceName test \
    --DBInstanceId postgres-apzvwncr
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

