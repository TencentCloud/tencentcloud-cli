**Example 1: 创建模型路由实例**



Input: 

```
tccli clb CreateModelRouter --cli-unfold-argument  \
    --ModelRouterType Enterprise \
    --ModelRouterName 模型路由实例 \
    --NetworkType Intranet \
    --Port 80 \
    --Schema HTTP \
    --SubnetId subnet-2cxt138a \
    --VpcId vpc-fc7eyow9 \
    --ClientToken 3e727335-f94c-468f-9989-21759a3b6de8
```

Output: 
```
{
    "Response": {
        "ModelRouterId": "cmr-g6rpjqmg",
        "RequestId": "406dfed3-ad8e-44d2-b742-c3b5c36dc060"
    }
}
```

