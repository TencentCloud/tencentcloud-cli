**Example 1: 取消漏洞扫描忽略漏洞**



Input: 

```
tccli tcss DeleteIgnoreVul --cli-unfold-argument  \
    --List.0.PocID "poc_id"
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

