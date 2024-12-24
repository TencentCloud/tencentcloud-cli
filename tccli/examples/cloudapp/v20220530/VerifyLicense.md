**Example 1: 从软件进程读取 LICENSE**

软件进程对接 LICENSE 后，通过运行时角色申请临时密钥来调用，获取对应的 LICENSE 信息。

获取到 LICENSE 后，请注意校验 LicenseStatus 是否有效，无效时软件可根据策略拒绝服务或者提供降级服务。同时，LICENSE 包含用户购买的规格信息，软件可根据规格来做运行的约束。

对接 LICENSE 的详细方案，请参考文档：
* [对接 LICENSE](https://cloud.tencent.com/document/product/1689/109428)
* [通过运行时角色调用云 API](https://cloud.tencent.com/document/product/1689/109427)

Input: 

```
tccli cloudapp VerifyLicense --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "License": {
            "LicenseId": "LICENSE_CLOUDAPP_A95275D8",
            "LicenseMode": "Subscription",
            "LicenseStatus": "Active",
            "ProviderId": 1,
            "SoftwarePackageId": "pkg-kby01bv4",
            "SoftwarePackageVersion": "1.0.0",
            "AuthorizedUserUin": "100008888888",
            "AuthorizedCloudappId": "cloudapp",
            "AuthorizedCloudappRoleId": "4000008000060000",
            "AuthorizedSpecification": [
                {
                    "ParamKey": "user_scale",
                    "ParamValue": "100",
                    "ParamKeyName": "用户规模",
                    "ParamValueName": "100人"
                }
            ],
            "BillingMode": 1,
            "LifeSpan": 1,
            "IssueDate": "2020-09-22T00:00:00+00:00",
            "ActivationDate": "2020-09-22T00:00:00+00:00",
            "ExpirationDate": "2020-09-23T00:00:00+00:00",
            "LifeSpanUnit": "D"
        },
        "RequestId": "845c8910-b0af-499e-87cd-f7dcc93a595a"
    }
}
```

