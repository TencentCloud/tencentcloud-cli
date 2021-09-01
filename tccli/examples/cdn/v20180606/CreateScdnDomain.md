**Example 1: 创建SCDN域名**



Input: 

```
tccli cdn CreateScdnDomain --cli-unfold-argument  \
    --Domain www.test.com \
    --Waf.Switch on \
    --CC.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "08b287d9-6342-4b70-9ec7-201efcd93b9d",
        "Result": "Success"
    }
}
```

