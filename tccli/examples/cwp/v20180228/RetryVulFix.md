**Example 1: 示例**

漏洞修复失败时，重试修复

Input: 

```
tccli cwp RetryVulFix --cli-unfold-argument  \
    --VulId 1 \
    --Quuid 1c26308c-5493-4eaf-a817-112ec25f499e \
    --FixId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "f14ce73f-50d7-4c36-af1d-fc33dae510c4"
    }
}
```

