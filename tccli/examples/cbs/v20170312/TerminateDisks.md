**Example 1: 批量退还云硬盘**

销毁两块云硬盘

Input: 

```
tccli cbs TerminateDisks --cli-unfold-argument  \
    --DiskIds disk-g27hqeo2 disk-lzrg2pwi
```

Output: 
```
{
    "Response": {
        "RequestId": "52c965d2-5deb-459a-8b5a-b3b9a1376544"
    }
}
```

