**Example 1: 查询资源包规格**

查询资源包规格


Input: 

```
tccli cynosdb DescribeResourcePackageSaleSpec --cli-unfold-argument  \
    --InstanceType abc \
    --PackageRegion abc \
    --PackageType abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Detail": [
            {
                "PackageRegion": "abc",
                "PackageType": "abc",
                "PackageVersion": "abc",
                "MinPackageSpec": 0,
                "MaxPackageSpec": 0,
                "ExpireDay": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

