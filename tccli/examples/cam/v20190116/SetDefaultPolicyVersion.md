**Example 1: 设置一个策略生效的策略版本**

本示例将设置一个策略生效的策略版本。

Input: 

```
tccli cam SetDefaultPolicyVersion --cli-unfold-argument  \
    --PolicyId 17698703 \
    --VersionId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "60e60a86-af67-4bbe-8377-7024a0e1d4c7"
    }
}
```

