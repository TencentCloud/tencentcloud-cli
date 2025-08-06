**Example 1: 创建 API 资源**

新建一个 API 资源。

Input: 

```
tccli teo CreateSecurityAPIResource --cli-unfold-argument  \
    --ZoneId zone-123sfakjf \
    --APIResources.0.Name test2 \
    --APIResources.0.Path /ava \
    --APIResources.0.APIServiceIds apisrv-123233399 \
    --APIResources.0.Methods POST PUT \
    --APIResources.0.RequestConstraint ${http.request.body.form['operationType']} in ['id.dana.order.listAl']
```

Output: 
```
{
    "Response": {
        "APIResourceIds": [
            "apires-1232382313"
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

