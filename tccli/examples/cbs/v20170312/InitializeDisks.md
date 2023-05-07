**Example 1: 重新初始化云硬盘**

将云硬盘ID为disk-ixya2wzy的云盘重新初始化为刚创建时的状态。

Input: 

```
tccli cbs InitializeDisks --cli-unfold-argument  \
    --DiskIds disk-ixya2wzy
```

Output: 
```
{
    "Response": {
        "RequestId": "aafa71a0-ed62-0fac-3ebf-5a1f808d1085"
    }
}
```

