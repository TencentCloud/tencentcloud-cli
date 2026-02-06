**Example 1: 购买套餐**



Input: 

```
tccli igtm CreatePackageAndPay --cli-unfold-argument  \
    --DealType CREATE \
    --GoodsType ULTIMATE \
    --GoodsNum 1 \
    --AutoRenew 1 \
    --TimeSpan 1 \
    --AutoVoucher 1
```

Output: 
```
{
    "Response": {
        "RequestId": "079d26c3-15a0-4ce0-836d-7307776860e1",
        "ResourceIds": [
            "ins-ojwefnyfigv"
        ]
    }
}
```

**Example 2: 续费套餐**



Input: 

```
tccli igtm CreatePackageAndPay --cli-unfold-argument  \
    --DealType RENEW \
    --GoodsType ULTIMATE \
    --GoodsNum 1 \
    --AutoRenew 1 \
    --ResourceId ins-ojwefnyfigv \
    --TimeSpan 1 \
    --AutoVoucher 1
```

Output: 
```
{
    "Response": {
        "RequestId": "079d26c3-15a0-4ce0-836d-7307776860e1",
        "ResourceIds": [
            "ins-ojwefnyfigv"
        ]
    }
}
```

**Example 3: 变配套餐**



Input: 

```
tccli igtm CreatePackageAndPay --cli-unfold-argument  \
    --DealType MODIFY \
    --GoodsType STANDARD \
    --GoodsNum 1 \
    --AutoRenew 1 \
    --ResourceId ins-lntftyrifqx \
    --TimeSpan 1 \
    --NewPackageType ULTIMATE \
    --AutoVoucher 1
```

Output: 
```
{
    "Response": {
        "RequestId": "183a7455-6a2c-4e17-816d-e45e880230fe",
        "ResourceIds": [
            "ins-lntftyrifqx"
        ]
    }
}
```

