**Example 1: 查询边缘单元NodeUnit列表**



Input: 

```
tccli iecp DescribeNodeUnit --cli-unfold-argument  \
    --EdgeUnitId 1 \
    --NodeGroupName test
```

Output: 
```
{
    "Response": {
        "RequestId": "72d540a0-ed11-4370-b977-96c6c224a1d8",
        "TotalCount": 1,
        "NodeGridInfo": [
            {
                "Id": 0,
                "NodeUnitName": "testunit",
                "NodeList": []
            }
        ]
    }
}
```

