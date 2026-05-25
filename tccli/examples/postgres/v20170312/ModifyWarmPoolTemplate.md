**Example 1: 修改资源池预热模版启停状态**



Input: 

```
tccli postgres ModifyWarmPoolTemplate --cli-unfold-argument  \
    --TemplateName test_my_template2 \
    --Enabled 0
```

Output: 
```
{
    "Response": {
        "Enabled": 0,
        "TemplateName": "test_my_template2",
        "RequestId": "ea1876a5-d367-4d1f-af5e-270d878e22d3"
    }
}
```

