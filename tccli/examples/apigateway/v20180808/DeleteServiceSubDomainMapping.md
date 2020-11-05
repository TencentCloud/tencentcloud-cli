**Example 1: Deleting the path mapping of custom domain name**



Input: 

```
tccli apigateway DeleteServiceSubDomainMapping --cli-unfold-argument  \
    --ServiceId service-19c5fnhy\
    --SubDomain xxxxxxx\
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

