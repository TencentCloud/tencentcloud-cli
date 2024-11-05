**Example 1: 查询资源包规格**

查询资源包规格


Input: 

```
tccli cynosdb DescribeResourcePackageSaleSpec --cli-unfold-argument  \
    --InstanceType cynosdb-serverless \
    --PackageRegion china \
    --PackageType CCU \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Detail": [
            {
                "PackageRegion": "china",
                "PackageType": "CCU",
                "PackageVersion": "common",
                "MinPackageSpec": 50,
                "MaxPackageSpec": 100,
                "ExpireDay": 180
            }
        ],
        "RequestId": "93c96481-e37c-49f7-aeb5-907ee97a198c"
    }
}
```

