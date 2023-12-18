**Example 1: DescribeServicesByCert**

通过证书获取服务列表

Input: 

```
tccli apigateway DescribeServicesByCert --cli-unfold-argument  \
    --Status 0 \
    --Offset 0 \
    --Limit 10 \
    --CloudCertIds xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "ea6a8dba-c935-4708-a446-af8b7f186d6d"
    }
}
```

