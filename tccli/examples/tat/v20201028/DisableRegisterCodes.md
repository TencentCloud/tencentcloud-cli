**Example 1: 禁用注册码**

根据注册码ID禁用注册码。

Input: 

```
tccli tat DisableRegisterCodes --cli-unfold-argument  \
    --RegisterCodeIds abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

