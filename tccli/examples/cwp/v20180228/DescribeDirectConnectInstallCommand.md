**Example 1: 清理主机信息**



Input: 

```
tccli cwp DescribeDirectConnectInstallCommand --cli-unfold-argument  \
    --RegionCode sz \
    --VpcId vpc-dsda \
    --ExpireDate 2020-09-22
```

Output: 
```
{
    "Response": {
        "Ip": "10.0.0.11",
        "Token": "708cae4cf814c3deda4208da228fad4e",
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

