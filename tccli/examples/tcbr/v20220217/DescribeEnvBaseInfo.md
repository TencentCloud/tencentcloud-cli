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
        "RequestId": "",
        "EnvBaseInfo": {
            "PackageType": "Trial",
            "CreateTime": "2022-05-27 15:00:00",
            "EnvId": "prod-0g8ki95z117f177d"
        }
    }
}
```

