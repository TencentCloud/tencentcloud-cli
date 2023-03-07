**Example 1: 禁用检测策略**

禁用检测策略

Input: 

```
tccli cwp ModifyBaselinePolicyState --cli-unfold-argument  \
    --IsEnabled 0 \
    --PolicyId 259
```

Output: 
```
{
    "Response": {
        "RequestId": "c4306e95-f45b-408b-aff0-b3cc16f673e1"
    }
}
```

**Example 2: 使能策略**

使能策略

Input: 

```
tccli cwp ModifyBaselinePolicyState --cli-unfold-argument  \
    --IsEnabled 0 \
    --PolicyId 259
```

Output: 
```
{
    "Response": {
        "RequestId": "ca6e6339-34ba-4c0d-90ac-3c4a6ea6d383"
    }
}
```

