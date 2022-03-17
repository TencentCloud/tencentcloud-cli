**Example 1: 查询预添加节点**



Input: 

```
tccli iecp DescribeEdgeSnNodes --cli-unfold-argument  \
    --EdgeUnitId 100026
```

Output: 
```
{
    "Response": {
        "RequestId": "c9f0bda5-0644-4eac-8d95-f4732eb78e8d",
        "TotalCount": 1,
        "NodeSet": [
            {
                "Id": 91,
                "Name": "snnode",
                "IsUsed": false,
                "CreateTime": "2022-03-09 17:48:15",
                "Remark": "20220911",
                "SN": "SN2232323"
            }
        ]
    }
}
```

