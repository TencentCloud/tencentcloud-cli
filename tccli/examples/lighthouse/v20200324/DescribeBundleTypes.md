**Example 1: 国内站查询套餐类型**

国内站查询套餐类型

Input: 

```
tccli lighthouse DescribeBundleTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BundleTypeDetailSet": [
            {
                "BundleType": "STARTER_BUNDLE",
                "Description": "入门型"
            },
            {
                "BundleType": "GENERAL_BUNDLE",
                "Description": "通用型"
            },
            {
                "BundleType": "ENTERPRISE_BUNDLE",
                "Description": "企业型"
            },
            {
                "BundleType": "STORAGE_BUNDLE",
                "Description": "存储型"
            },
            {
                "BundleType": "EXCLUSIVE_BUNDLE",
                "Description": "专属型"
            },
            {
                "BundleType": "HK_EXCLUSIVE_BUNDLE",
                "Description": "香港专属型"
            },
            {
                "BundleType": "CAREFREE_BUNDLE",
                "Description": "无忧型"
            },
            {
                "BundleType": "BEFAST_BUNDLE",
                "Description": "蜂驰型"
            }
        ],
        "RequestId": "bc561f9a-5df5-4af5-9d5f-64881c295fa6"
    }
}
```

**Example 2: 国际站查询套餐类型**

国际站查询套餐类型

Input: 

```
tccli lighthouse DescribeBundleTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BundleTypeDetailSet": [
            {
                "BundleType": "STARTER_BUNDLE",
                "Description": "Starter Type"
            },
            {
                "BundleType": "GENERAL_BUNDLE",
                "Description": "General Type"
            },
            {
                "BundleType": "ENTERPRISE_BUNDLE",
                "Description": "Enterprise Type"
            },
            {
                "BundleType": "STORAGE_BUNDLE",
                "Description": "Storage Type"
            },
            {
                "BundleType": "EXCLUSIVE_BUNDLE",
                "Description": "Exclusive Type"
            },
            {
                "BundleType": "HK_EXCLUSIVE_BUNDLE",
                "Description": "HK Exclusive Type"
            },
            {
                "BundleType": "CAREFREE_BUNDLE",
                "Description": "Carefree Type"
            },
            {
                "BundleType": "BEFAST_BUNDLE",
                "Description": "BeFast Type"
            }
        ],
        "RequestId": "333a0eea-c2d5-49f1-892e-c296367acde9"
    }
}
```

