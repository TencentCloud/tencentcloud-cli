**Example 1: GetCrowdStatusById**



Input: 

```
tccli zj GetCrowdStatusById --cli-unfold-argument  \
    --License KA3431QZPU \
    --CrowdID 47
```

Output: 
```
{
    "Response": {
        "Data": {
            "CrowdID": 47,
            "Name": "人群包名称",
            "Status": 2
        },
        "RequestId": "111111"
    }
}
```

