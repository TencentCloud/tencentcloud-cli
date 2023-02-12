**Example 1: 创建命名空间**

在企业版中创建命名空间

Input: 

```
tccli tcr CreateNamespace --cli-unfold-argument  \
    --NamespaceName mytest \
    --IsPublic true \
    --IsAutoScan true \
    --IsPreventVUL true \
    --Severity low \
    --RegistryId tcr-okmj78
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

