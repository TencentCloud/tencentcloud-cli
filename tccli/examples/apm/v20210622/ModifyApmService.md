**Example 1: 修改应用**

修改应用

Input: 

```
tccli apm ModifyApmService --cli-unfold-argument  \
    --ServiceID svc-SgUX9ueaj \
    --ServiceDescription 测试用的 \
    --Tags.0.Key user \
    --Tags.0.Value developer
```

Output: 
```
{
    "Response": {
        "RequestId": "4f4bd026-6c87-429f-b9c5-0dd5afd0af46"
    }
}
```

