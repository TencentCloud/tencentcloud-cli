**Example 1: 导入公共应用到指定项目**



Input: 

```
tccli omics ImportCommonApplication --cli-unfold-argument  \
    --CommonAppUuid 0de1b4ae-1543-4882-8bae-b5ee87968bc5 \
    --CommonAppNewName scBERT_test_1 \
    --ProjectId prj-efficient-maroon-slug-075080 \
    --Type NEXTFLOW \
    --NextflowVersion v24.04.3
```

Output: 
```
{
    "Response": {
        "ApplicationId": "app-unique-olive-yeti-950894",
        "RequestId": "382e367e-255d-4572-b1b6-7e4c2bddc5e0"
    }
}
```

