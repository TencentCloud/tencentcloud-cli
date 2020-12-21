**Example 1: 设置预置并发**



Input: 

```
tccli scf PutProvisionedConcurrencyConfig --cli-unfold-argument  \
    --FunctionName test \
    --Qualifier 1 \
    --VersionProvisionedConcurrencyNum 10
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

