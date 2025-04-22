**Example 1: 新建访问白名单规则**

新建访问白名单规则

Input: 

```
tccli bh CreateAccessWhiteListRule --cli-unfold-argument  \
    --Source 10.10.10.1 \
    --Remark 规则1
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

