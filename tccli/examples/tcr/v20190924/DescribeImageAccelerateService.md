**Example 1: 查询镜像加速服务状态**



Input: 

```
tccli tcr DescribeImageAccelerateService --cli-unfold-argument  \
    --RegistryId tcr-dg284imq
```

Output: 
```
{
    "Response": {
        "CFSVIP": "",
        "IsEnable": false,
        "RequestId": "dde9bf37-d34c-4c7a-bf0d-a11531ce6ebe",
        "Status": ""
    }
}
```

