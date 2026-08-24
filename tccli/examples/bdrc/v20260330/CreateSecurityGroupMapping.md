**Example 1: 创建安全组映射**



Input: 

```
tccli bdrc CreateSecurityGroupMapping --cli-unfold-argument  \
    --SrcSecurityGroupId sg-5mmgq8xt \
    --TargetSecurityGroupId sg-5mmgq8xt \
    --SitePairId sitepair-3k23fkmn
```

Output: 
```
{
    "Response": {
        "RequestId": "839cca5f-66e2-4765-b835-1059dc2be466"
    }
}
```

