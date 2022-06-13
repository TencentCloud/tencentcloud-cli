**Example 1: 查询实例公网访问入口状态**



Input: 

```
tccli tcr DescribeExternalEndpointStatus --cli-unfold-argument  \
    --RegistryId tcr-12345
```

Output: 
```
{
    "Response": {
        "RequestId": "55d06f7c-c488-4910-8f67-8d7f77f0fe0f",
        "Status": "Opened",
        "Reason": ""
    }
}
```

