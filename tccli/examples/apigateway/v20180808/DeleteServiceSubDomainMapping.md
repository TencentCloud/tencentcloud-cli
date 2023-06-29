**Example 1: 删除自定义域名的路径映射**

删除自定义域名的路径映射


Input: 

```
tccli apigateway DeleteServiceSubDomainMapping --cli-unfold-argument  \
    --ServiceId service-19c5fnhy \
    --SubDomain doagkfrf.flyfly.wang \
    --Environment test
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "1ab681ab-545a-4e71-91f1-8f1ea8ef13ad"
    }
}
```

