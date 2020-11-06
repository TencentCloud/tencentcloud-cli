**Example 1: 查询API版本列表**



Input: 

```
tccli tsf DescribeApiVersions --cli-unfold-argument  \
    --MicroserviceId ms-2vzprpyp \
    --Path /facade/supplier/test \
    --Method POST
```

Output: 
```
{
    "Response": {
        "RequestId": "8fa43626-954c-4892-875c-4c1d6a6ed59a",
        "Result": [
            {
                "ApplicationName": "prod_supplier",
                "ApplicationId": "application-gvkw2ejv",
                "PkgVersion": "jenkins-prod-supplier-1"
            }
        ]
    }
}
```

