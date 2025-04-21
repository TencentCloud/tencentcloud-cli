**Example 1: 获取终端设备特权码或者卸载码**

获取终端设备特权码或者卸载码

Input: 

```
tccli ioa CreatePrivilegeCode --cli-unfold-argument  \
    --Mid BC5184BEC838B96B29CE8105EC071B88663283537
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": "981066"
        },
        "RequestId": "1658388067.5420978"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa CreatePrivilegeCode --cli-unfold-argument  \
    --Mid 75129D715480905B6A9C4569893C7634663C2D68
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": "417484"
        },
        "RequestId": "4f84848e-26e7-4d01-80d9-2d3b6d14d697"
    }
}
```

