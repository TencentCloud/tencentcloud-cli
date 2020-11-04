**Example 1: 关闭serverless外网**



Input: 

```
tccli postgres CloseServerlessDBExtranetAccess --cli-unfold-argument  \
    --DBInstanceId postgres-apzvwncr\
    --DBInstanceName test
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

