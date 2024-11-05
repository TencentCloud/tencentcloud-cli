**Example 1: 编辑防篡改url**



Input: 

```
tccli waf ModifyAntiFakeUrl --cli-unfold-argument  \
    --Domain www.test.com \
    --Name rulename \
    --Uri http://zanyang.qcloudwaf.com/index.html \
    --Id 11011
```

Output: 
```
{
    "Response": {
        "RequestId": "32e5e790-5999-4aa6-a3cb-34ed4c570d14",
        "Result": "success"
    }
}
```

