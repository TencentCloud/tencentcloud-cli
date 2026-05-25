**Example 1: 删除资源池预热模版**



Input: 

```
tccli postgres DeleteWarmPoolTemplate --cli-unfold-argument  \
    --TemplateName test-zero-target-0522
```

Output: 
```
{
    "Response": {
        "TemplateName": "test-zero-target-0522",
        "RequestId": "1874e337-1198-4fc9-a7e5-7d24b296233b"
    }
}
```

