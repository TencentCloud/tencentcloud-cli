**Example 1: 指定密码进行轮转密码刷新**

指定密码进行轮转密码刷新

Input: 

```
tccli cdb ResetInstancePassword --cli-unfold-argument  \
    --UserResourceId cdb-7qmr5idl \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount ssmtest1 \
    --Password 123456abcd1 \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "RequestId": "0"
    }
}
```

