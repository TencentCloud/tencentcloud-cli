**Example 1: 修改指定 API 服务**

修改某个已有的 API 服务的关联域名、规则名和基础路径。

Input: 

```
tccli teo ModifySecurityAPIService --cli-unfold-argument  \
    --ZoneId zone-123sfakjf \
    --APIServices.0.Id apisrv-1230001001 \
    --APIServices.0.Name test \
    --APIServices.0.BasePath /tt
```

Output: 
```
{
    "Response": {
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

