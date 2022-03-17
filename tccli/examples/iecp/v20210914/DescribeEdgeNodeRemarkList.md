**Example 1: 获取边缘集群节点备注列表**



Input: 

```
tccli iecp DescribeEdgeNodeRemarkList --cli-unfold-argument  \
    --EdgeUnitId 100026
```

Output: 
```
{
    "Response": {
        "RequestId": "b15640f7-a4e4-4ce4-b418-1b864ba7569d",
        "Remarks": [
            "20220911"
        ]
    }
}
```

