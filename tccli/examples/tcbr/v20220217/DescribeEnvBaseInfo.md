**Example 1: 查询环境基础信息**



Input: 

```
tccli tcbr DescribeEnvBaseInfo --cli-unfold-argument  \
    --EnvId prod-0g8ki95z117f177d
```

Output: 
```
{
    "Response": {
        "EnvBaseInfo": {
            "EnvId": "en-sdf",
            "PackageType": "package",
            "VpcId": "vpc-sdff",
            "CreateTime": "2023-12-12 10:00:00",
            "Alias": "sdf",
            "Status": "creating",
            "Region": "ap-shanghai",
            "EnvType": "tcbr",
            "SubnetIds": ""
        },
        "RequestId": "sdfdsgdg"
    }
}
```

