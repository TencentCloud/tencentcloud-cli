**Example 1: 查看第三方节点列表**



Input: 

```
tccli tke DescribeExternalNode --cli-unfold-argument  \
    --ClusterId cls-abcd1234 \
    --NodePoolId np-abcd1234
```

Output: 
```
{
    "Response": {
        "Nodes": [
            {
                "CreatedTime": "2021-04-29T06:30:44Z",
                "IP": "10.0.0.135",
                "Name": "lkongtest",
                "NodePoolId": "np-0nwzqj10",
                "Location": "gz"
            }
        ],
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "TotalCount": 1
    }
}
```

