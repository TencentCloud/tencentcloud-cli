**Example 1: 更新一个addon**

获取一个addon的版本和参数

Input: 

```
tccli tke UpdateAddon --cli-unfold-argument  \
    --ClusterId cls-123deabc \
    --AddonName cbs \
    --AddonVersion 1.1.0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

