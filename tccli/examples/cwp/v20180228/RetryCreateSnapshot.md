**Example 1: 示例**

修复漏洞时快照创建失败重新创建

Input: 

```
tccli cwp RetryCreateSnapshot --cli-unfold-argument  \
    --FixId 1 \
    --Quuid "xxxxxx" \
    --Id 12
```

Output: 
```
{
    "Response": {
        "RequestId": "f14ce73f-50d7-4c36-af1d-fc33dae510c4"
    }
}
```

