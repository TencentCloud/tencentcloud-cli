**Example 1: 策略绑定标签**

策略绑定标签

Input: 

```
tccli monitor BindingPolicyTag --cli-unfold-argument  \
    --Module monitor \
    --GroupId 678 \
    --PolicyId policy-gqz8m9uq \
    --ServiceType cvm \
    --Tag.Key region \
    --Tag.Value gz
```

Output: 
```
{
    "Response": {
        "RequestId": "0dbb66c2-1111-1111-1111-11111111111"
    }
}
```

