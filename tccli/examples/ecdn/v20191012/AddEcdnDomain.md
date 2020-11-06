**Example 1: 新增加速域名**



Input: 

```
tccli ecdn AddEcdnDomain --cli-unfold-argument  \
    --Domain www.test.com \
    --Origin.Origins 2.2.2.2 \
    --Area global
```

Output: 
```
{
    "Response": {
        "RequestId": "23cd4005-496f-4bc4-87d8-ab348d5b0c17"
    }
}
```

