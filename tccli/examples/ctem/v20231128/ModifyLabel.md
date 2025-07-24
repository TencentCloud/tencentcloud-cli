**Example 1: 编辑标签**

编辑标签

Input: 

```
tccli ctem ModifyLabel --cli-unfold-argument  \
    --Id 8706 \
    --CustomerId 100162 \
    --Module asset \
    --Labels {"user_input_123":["测试"]}
```

Output: 
```
{
    "Response": {
        "RequestId": "fe8d21e4-73e7-425a-aebf-4a97396af03b"
    }
}
```

