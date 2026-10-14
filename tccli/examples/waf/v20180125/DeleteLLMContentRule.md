**Example 1: 删除大模型内容防护规则**

删除大模型内容防护规则

Input: 

```
tccli waf DeleteLLMContentRule --cli-unfold-argument  \
    --Domain clar11.waf.com \
    --Ids 5200027919
```

Output: 
```
{
    "Response": {
        "RequestId": "db1b81e9-748e-4b19-a216-9f210060ab1d"
    }
}
```

