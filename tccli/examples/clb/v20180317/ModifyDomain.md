**Example 1: Modifying the domain name of a forwarding rule under an HTTP listener**



Input: 

```
tccli clb ModifyDomain --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0\
    --ListenerId lbl-d1ubsydq\
    --Domain foo.net\
    --NewDomain bar.net
```

Output: 
```
{
    "Response": {
        "RequestId": "db141822-c025-4765-88d4-02bdec0e67ed"
    }
}
```

