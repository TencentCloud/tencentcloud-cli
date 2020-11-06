**Example 1: 创建一条转发规则**



Input: 

```
tccli clb CreateRule --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-4fbxq45k \
    --Rules.0.Domain foo.net \
    --Rules.0.Url /bar
```

Output: 
```
{
    "Response": {
        "LocationIds": [
            "loc-ho6lvh8m"
        ],
        "RequestId": "6c915c06-53e0-4717-9358-09b32cf47f08"
    }
}
```

