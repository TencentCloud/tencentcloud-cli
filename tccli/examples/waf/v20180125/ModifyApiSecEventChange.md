**Example 1: test111**

weraza

Input: 

```
tccli waf ModifyApiSecEventChange --cli-unfold-argument  \
    --UserName ddp \
    --EventIdList api_test \
    --Remark test \
    --Mode 2 \
    --ApiNameList.0.Domain www.test.com \
    --ApiNameList.0.Method POST \
    --ApiNameList.0.ApiName aaa
```

Output: 
```
{
    "Response": {
        "RequestId": "ac576aa3-4a4c-4a8e-81c0-c650c139d074"
    }
}
```

