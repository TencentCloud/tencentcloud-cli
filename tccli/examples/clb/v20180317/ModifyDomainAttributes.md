**Example 1: 修改七层监听器下域名的相关属性**

修改七层监听器下域名的相关属性

Input: 

```
tccli clb ModifyDomainAttributes --cli-unfold-argument  \
    --Domain foo.net \
    --ListenerId lbl-n8mb2r3a \
    --LoadBalancerId lb-1wvl0ejw
```

Output: 
```
{
    "Response": {
        "RequestId": "db141822-c025-4765-88d4-02bdec0e67ed"
    }
}
```

