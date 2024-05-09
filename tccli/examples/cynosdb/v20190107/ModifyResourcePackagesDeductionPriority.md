**Example 1: ModifyResourcePackagesDeductionPriority**

修改已绑定资源包抵扣优先级

Input: 

```
tccli cynosdb ModifyResourcePackagesDeductionPriority --cli-unfold-argument  \
    --PackageType CCU \
    --ClusterId cynosdbmysql-abcd1234 \
    --DeductionPriorities.0.PackageId package-abcd1234 \
    --DeductionPriorities.0.DeductionPriority 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

