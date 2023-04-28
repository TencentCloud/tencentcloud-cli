**Example 1: 添加品牌**

添加品牌

Input: 

```
tccli bma CreateBPBrand --cli-unfold-argument  \
    --CompanyName 企业名称 \
    --BrandName 品牌名称 \
    --BrandLogo 品牌Logo \
    --Phone 联系电话 \
    --License 营业执照 \
    --Authorization 授权书 \
    --TrademarkNames 商标名称 \
    --Trademarks 商标证明 \
    --IsTransfers 1 \
    --Transfers 转让证明 \
    --ProtectURLs qq.com baidu.com \
    --ProtectAPPs 王者荣耀 和平精英 \
    --ProtectOfficialAccounts 人民日报 广东日报 \
    --ProtectMiniPrograms 粤省事
```

Output: 
```
{
    "Response": {
        "CompanyId": 123,
        "RequestId": "xxx"
    }
}
```

