**Example 1: 修改七层监听器下域名的相关属性**



Input: 

```
tccli clb ModifyDomainAttributes --cli-unfold-argument  \
    --LoadBalancerId lb-1wvl0ejw \
    --ListenerId lbl-n8mb2r3a \
    --Domain foo.net
```

Output: 
```
{
    "Response": {
        "RequestId": "db141822-c025-4765-88d4-02bdec0e67ed"
    }
}
```

