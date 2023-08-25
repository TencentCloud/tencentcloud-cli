**Example 1: cynos解绑资源包**

cynos解绑资源包

Input: 

```
tccli cynosdb UnbindClusterResourcePackages --cli-unfold-argument  \
    --ClusterId abc \
    --PackageIds package-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

