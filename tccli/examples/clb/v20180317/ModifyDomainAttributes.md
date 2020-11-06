**Example 1: Modifying the domain name attributes of a layer-7 listener**



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

