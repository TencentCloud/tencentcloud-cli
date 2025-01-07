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
            "EnvId": "abc",
            "PackageType": "abc",
            "VpcId": "abc",
            "CreateTime": "abc",
            "Alias": "abc",
            "Status": "abc",
            "Region": "abc",
            "EnvType": "abc",
            "SubnetIds": "abc"
        },
        "RequestId": "abc"
    }
}
```

