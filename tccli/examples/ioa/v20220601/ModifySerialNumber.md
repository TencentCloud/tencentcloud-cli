**Example 1: 示例1**



Input: 

```
tccli ioa ModifySerialNumber --cli-unfold-argument  \
    --Mid 46466be048df48f3bbb5bd1f8a42a069635247D3 \
    --SerialNum AAABBCCCDDDD
```

Output: 
```
{
    "Response": {
        "RequestId": "9386b1b4-0425-469d-8470-6e83b5c41c30"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa ModifySerialNumber --cli-unfold-argument  \
    --Mid 75129D715480905B6A9C4569893C7634663C2D68 \
    --SerialNum 12344
```

Output: 
```
{
    "Response": {
        "RequestId": "be5a748d-4aa4-4e1d-bb2d-6b6c0a78827d"
    }
}
```

