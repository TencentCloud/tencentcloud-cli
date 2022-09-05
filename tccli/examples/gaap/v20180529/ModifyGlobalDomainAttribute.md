**Example 1: 修改域名属性**



Input: 

```
tccli gaap ModifyGlobalDomainAttribute --cli-unfold-argument  \
    --ProjectId 0 \
    --DefaultValue 1.1.1.1 \
    --DomainId test.com \
    --Alias test
```

Output: 
```
{
    "Response": {
        "RequestId": "19a021f8-dff3-4890-8e7a-ed5054e22e49"
    }
}
```

