**Example 1: 修改ip惩罚配置**

修改ip惩罚配置

Input: 

```
tccli waf ModifyWafAutoDenyRules --cli-unfold-argument  \
    --Domain test.test.com \
    --TimeThreshold 0 \
    --DenyTimeThreshold 0 \
    --AttackThreshold 0 \
    --DefenseStatus 0
```

Output: 
```
{
    "Response": {
        "Success": {
            "Code": "Success",
            "Message": "Success"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

