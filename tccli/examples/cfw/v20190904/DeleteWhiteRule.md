**Example 1: 按 WhiteId 删除**

批量删除时在数组中传入多个 WhiteId。

Input: 

```
tccli cfw DeleteWhiteRule --cli-unfold-argument  \
    --WhiteIdList wl-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "00000000-0000-4000-8000-000000000001"
    }
}
```

