**Example 1: 检查推理服务名称是否重复**



Input: 

```
tccli dlc CheckServiceName --cli-unfold-argument  \
    --ServiceName test-abcd
```

Output: 
```
{
    "Response": {
        "Exists": false,
        "RequestId": "e46ed47c-1f20-4dab-849e-0da9a08f2dd4"
    }
}
```

