**Example 1: 参考示例**

正确的示例

Input: 

```
tccli billing SetResourceRenewStrategyInner --cli-unfold-argument  \
    --OwnerUin 302000020582 \
    --Operator 302000020582 \
    --ProductCode p_tencentmeeting_saas \
    --SubProductCode sp_tencentmeeting_saas_prov2 \
    --ReferenceId 4a2de158ccef369cb5de5f8bd \
    --ResourceIds 302000020582_2024110418004318007093_100 \
    --RegionApCode ap-guangzhou \
    --ResourceRenewStrategy strategy_vip_no_auto
```

Output: 
```
{
    "Response": {
        "ReferenceId": "4a2de158ccef369cb5de5f8bd",
        "RequestId": "53f187ec-13f4-4d32-8306-d8acc19578fd",
        "ResourceSet": []
    }
}
```

