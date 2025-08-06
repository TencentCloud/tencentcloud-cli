**Example 1: 查询报价产品名称与计费产品四层匹配关系**

查询报价产品名称与计费产品四层匹配关系

Input: 

```
tccli billing DescribeCPQBillingMapping --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1aa76e23-91a1-40bc-a9b0-671f8a7c0489",
        "ResourceSpuSet": [
            {
                "BusinessCode": "p_011691",
                "BusinessNameEn": "Tencent Kubernetes Engine",
                "BusinessNameZh": "容器服务 TKE",
                "CategoryNameEn": "ResouceFee&ServiceFee",
                "CategoryNameZh": "资源费+增值费模式（同一个机型，资源费+增值费模式或增值费模式二选一，不能重复选择）",
                "ComponentCode": "",
                "ComponentNameEn": "",
                "ComponentNameZh": "",
                "ItemCode": "",
                "ItemNameEn": "",
                "ItemNameZh": "",
                "ProductCode": "sp_011691_tke_hn_c4",
                "ProductNameEn": "TKE_NativeNode_C4",
                "ProductNameZh": "容器服务TKE_原生节点_C4",
                "SpuNameEn": "Postpaid TKE native node - Computing C4",
                "SpuNameZh": "TKE原生节点-计算型C4-后付费"
            }
        ],
        "Total": 3819
    }
}
```

