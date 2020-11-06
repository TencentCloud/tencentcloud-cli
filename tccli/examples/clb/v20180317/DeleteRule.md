**Example 1: Deleting a forwarding rule**



Input: 

```
tccli clb DeleteRule --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-4fbxq45k \
    --Domain foo.net \
    --Url /bar2
```

Output: 
```
{
    "Response": {
        "RequestId": "ba2d4eb1-c7c5-480c-98e4-9b7b6a0fd498"
    }
}
```

