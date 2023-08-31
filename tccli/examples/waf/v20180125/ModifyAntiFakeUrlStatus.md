**Example 1: 切换防篡改开关**



Input: 

```
tccli waf ModifyAntiFakeUrlStatus --cli-unfold-argument  \
    --Domain test.com \
    --Status 0 \
    --Ids 123 345
```

Output: 
```
{
    "Response": {
        "RequestId": "c68bdee7-2c14-4bd3-ba41-cdf1421c0d0c"
    }
}
```

