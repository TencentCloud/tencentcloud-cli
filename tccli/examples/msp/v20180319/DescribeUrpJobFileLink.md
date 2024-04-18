**Example 1: 请求成功**

成功获得下载地址

Input: 

```
tccli msp DescribeUrpJobFileLink --cli-unfold-argument  \
    --Account divewang \
    --PlanID plan-lhgqFY2z
```

Output: 
```
{
    "Response": {
        "DownloadURL": "https://cpt-msp-dev-1258344699.cos.ap-shanghai.myqcloud.com/%2Ftest/console/1254098721/urp-Ye0I6J3c/urp-Ye0I6J3c_scan.xlsx?x-cos-security-token=hUfFTkpPGfP9i1ULqopJpJs4WTFfbp2ae68d3777a58766d37484fdf29b7b26a1B1DUlSIogJV60u4o5YDkrZjzQ9JdJK3q_H91Vkf7GmXAerCUBbrbUN3IlqLirlDJok6PaC9Fkx8ythtPlWHv3Np4Cvf85LXaLxF8ti9_zO2qw5eRpYNdPDkqPU4P4lVIgSGy-rPr8U2ufEIaJvE0p-c_GbwU0QMlwhhweXlve1pUovb8RbthFMvhebWP0RiCWiEq6dJBNNaCrj_5K3TLknnht2FbhEBGp27sCbI4nngXJkS1MtrzLka6V3EESYxMtTz1mZ2wH_oZlMdQm05XGvmZPFoupO6G5Fer1-S6WnM&q-sign-algorithm=sha1&q-ak=AKIDGu3ahh-0jkBECql8p0OsgNkuHpV_DzqTmlCtvI3OdQq2HxSTchgkZ4axnHlgt4U5&q-sign-time=1712647608%3B1712651208&q-key-time=1712647608%3B1712651208&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=1f3d5b339c3652c70295d17a733d3acd5cbd89a0",
        "RequestId": "db2b4bb3-f70d-45f9-8f8d-1cb56786847c"
    }
}
```

