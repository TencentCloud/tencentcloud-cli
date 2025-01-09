**Example 1: 查看安全网关**



Input: 

```
tccli tcb DescribeWxGateways --cli-unfold-argument  \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "Gateways": [
            {
                "AccessDomain": "",
                "AllowUncertified": 0,
                "AppId": 0,
                "AutoRenewFlag": 1,
                "CanDowngrade": false,
                "CanRenew": true,
                "CreateTime": "2023-11-23 10:27:31",
                "EnvId": "envid-xxx",
                "ExpireTime": "2024-12-23 23:59:59",
                "GatewayDesc": "",
                "GatewayId": "envid-xxx",
                "GatewayName": "gatewayname-xxx",
                "GatewayType": "wechat",
                "IsolateTime": "0000-00-00 00:00:00",
                "L5Addr": "",
                "LongAccessId": "",
                "PackageId": 2005,
                "PackageVersion": "testV2",
                "Region": "ap-shanghai",
                "Status": "success",
                "SubnetIds": [
                    "subnet-xxxx"
                ],
                "Uin": "100008561789",
                "UpdateTime": "2024-04-25 10:50:13",
                "VersionNumLimit": 3,
                "VpcId": "vpcid-xxxx",
                "WxAppId": "wxappid-xxxx"
            }
        ],
        "RequestId": "",
        "TotalCount": 1
    }
}
```

