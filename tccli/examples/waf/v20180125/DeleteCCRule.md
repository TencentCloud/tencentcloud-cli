**Example 1: Waf  CC V2 Delete接口**



Input: 

```
tccli waf DeleteCCRule --cli-unfold-argument  \
    --Domain test.com \
    --Name ccrulename \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "Data": "success",
        "RequestId": "d29f2d93-b894-4c04-b047-ea6470bc0acd"
    }
}
```

