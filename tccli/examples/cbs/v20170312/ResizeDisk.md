**Example 1: 将云硬盘扩容到200G**



Input: 

```
tccli cbs ResizeDisk --cli-unfold-argument  \
    --DiskId disk-lzrg2pwi \
    --DiskSize 200
```

Output: 
```
{
    "Response": {
        "RequestId": "adefc06d-2cf1-29f6-24a6-5a1f81b5c0ac"
    }
}
```

