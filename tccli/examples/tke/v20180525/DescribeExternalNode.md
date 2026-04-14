**Example 1: 查看注册节点列表**



Input: 

```
tccli tke DescribeExternalNode --cli-unfold-argument  \
    --ClusterId cls-2isgxkje \
    --NodePoolId np-bnd1ybd4
```

Output: 
```
{
    "Response": {
        "Nodes": [
            {
                "CreatedTime": "2026-03-19T08:10:41Z",
                "IP": "30.1.0.12",
                "Location": "",
                "Name": "node-30.1.0.12",
                "NodePoolId": "np-bnd1ybd4",
                "Reason": "",
                "Status": "Running",
                "Unschedulable": false
            }
        ],
        "TotalCount": 1,
        "RequestId": "6aa56aff-48d9-4296-89ae-9561d2fd4aa1"
    }
}
```

