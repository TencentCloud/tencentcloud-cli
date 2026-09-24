**Example 1: 删除空 Registry**

响应只带 RequestId。

Input: 

```
tccli ags DeleteRegistry --cli-unfold-argument  \
    --RegistryId reg-0123abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

