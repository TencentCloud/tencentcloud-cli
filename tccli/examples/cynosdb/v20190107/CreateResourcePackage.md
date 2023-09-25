**Example 1: 新购资源包**

新购资源包

Input: 

```
tccli cynosdb CreateResourcePackage --cli-unfold-argument  \
    --InstanceType cynosdb-serverless \
    --PackageRegion overseas \
    --PackageType CCU \
    --PackageVersion base \
    --PackageSpec 50 \
    --ExpireDay 180 \
    --PackageName 计算资源包-1 \
    --PackageCount 1
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "20230921633039500xxxxxx"
        ],
        "DealNames": [
            "20230921633039500xxxxxx"
        ],
        "RequestId": "a62d07af-xxxx-xxxx-xxxx-44b05196b40f"
    }
}
```

