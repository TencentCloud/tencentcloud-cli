**Example 1: 删除一个策略的策略版本**

本示例将删除一个策略的一个策略版本。

Input: 

```
tccli cam DeletePolicyVersion --cli-unfold-argument  \
    --VersionId 1 \
    --PolicyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "60e60a86-af67-4bbe-8377-7024a0e1d4c7"
    }
}
```

