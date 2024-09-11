**Example 1: 校验灾备可否回切**

校验灾备可否回切

Input: 

```
tccli cdb CheckDrInstanceRecovery --cli-unfold-argument  \
    --SrcInstanceId cdb-2t3lhacj \
    --DstInstanceId cdb-g3u3nf6v
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "CheckFlag": "success"
    }
}
```

