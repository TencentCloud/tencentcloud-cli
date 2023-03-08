**Example 1: 审批客户自有号码示例**

审批客户自有号码示例。

Input: 

```
tccli ccc ApplyCustomNumberList --cli-unfold-argument  \
    --ApplyId 0 \
    --Checker lulu \
    --CheckMsg ok \
    --State 0 \
    --SdkAppId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3651cda6-6501-4482-9f4e-8d0c9548a4db"
    }
}
```

