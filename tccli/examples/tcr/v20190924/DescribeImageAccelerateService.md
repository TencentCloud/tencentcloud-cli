**Example 1: 查询镜像加速服务状态**



Input: 

```
tccli tcr DescribeImageAccelerateService --cli-unfold-argument  \
    --RegistryId xxx
```

Output: 
```
{
    "Response": {
        "Status": "Completed",
        "CFSVIP": "10.1.1.1",
        "IsEnable": "true",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

