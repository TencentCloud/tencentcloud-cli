**Example 1: 删除一条转发规则**



Input: 

```
tccli clb DeleteRule --cli-unfold-argument  \
    --Url /bar2 \
    --Domain foo.net \
    --ListenerId lbl-4fbxq45k \
    --LoadBalancerId lb-cuxw2rm0
```

Output: 
```
{
    "Response": {
        "RequestId": "ba2d4eb1-c7c5-480c-98e4-9b7b6a0fd498"
    }
}
```

