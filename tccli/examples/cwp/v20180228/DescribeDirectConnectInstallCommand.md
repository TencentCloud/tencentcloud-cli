**Example 1: 清理主机信息**



Input: 

```
tccli cwp DescribeDirectConnectInstallCommand --cli-unfold-argument  \
    --RegionCode xx \
    --VpcId 1 \
    --ExpireDate 2020-09-22
```

Output: 
```
{
    "Response": {
        "Ip": "xx",
        "Token": "xx",
        "RequestId": "xx"
    }
}
```

