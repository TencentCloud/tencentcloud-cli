**Example 1: 刷新防篡改url**



Input: 

```
tccli waf FreshAntiFakeUrl --cli-unfold-argument  \
    --Domain www.test1.com \
    --Id 135
```

Output: 
```
{
    "Response": {
        "RequestId": "f6f281dd-5a8c-4525-90fb-9291170b804c",
        "Result": "success"
    }
}
```

