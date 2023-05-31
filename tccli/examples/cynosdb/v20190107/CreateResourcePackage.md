**Example 1: 新购资源包**

新购资源包

Input: 

```
tccli cynosdb CreateResourcePackage --cli-unfold-argument  \
    --InstanceType abc \
    --PackageRegion abc \
    --PackageType abc \
    --PackageVersion abc \
    --PackageSpec 0 \
    --ExpireDay 0 \
    --PackageName abc \
    --PackageCount 0
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "abc"
        ],
        "DealNames": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

