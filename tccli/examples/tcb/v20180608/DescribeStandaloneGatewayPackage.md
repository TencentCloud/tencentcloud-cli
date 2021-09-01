**Example 1: 查询小租户网关套餐信息**



Input: 

```
tccli tcb DescribeStandaloneGatewayPackage --cli-unfold-argument  \
    --EnvId env-test-xxx \
    --PackageVersion starter
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "StandaloneGatewayPackageList": [
            {
                "CPU": 0.25,
                "Mem": 1,
                "PackageVersion": "starter"
            }
        ],
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

