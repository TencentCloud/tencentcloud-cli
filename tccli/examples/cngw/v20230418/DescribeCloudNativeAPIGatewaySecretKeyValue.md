**Example 1: 查询密钥值**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewaySecretKeyValue --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --SecretKeyId secret-c75001b1
```

Output: 
```
{
    "Response": {
        "RequestId": "07313ba2-08a8-4933-9cd6-00052ffdd79a",
        "Result": "sk-xxxxxxxx"
    }
}
```

