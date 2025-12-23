**Example 1: 查询环境信息**



Input: 

```
tccli tcbr DescribeEnvBaseInfo --cli-unfold-argument  \
    --EnvId lowcode-0g8ki95z1xxxxx
```

Output: 
```
{
    "Response": {
        "EnvBaseInfo": {
            "EnvId": "lowcode-0g8ki95z1xxxxx",
            "PackageType": "Trial",
            "Alias": "default",
            "Status": "normal",
            "EnvType": "weda",
            "CreateTime": "2025-03-12 15:04:00",
            "Region": "ap-shanghai",
            "SubnetIds": "",
            "VpcId": ""
        },
        "RequestId": "27bfe819-1497-49b0-b0ec-xxxxxx",
        "IsExist": true
    }
}
```

