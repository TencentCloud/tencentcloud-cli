**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeTableByName --cli-unfold-argument  \
    --Name t1 \
    --DbName db1 \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993
```

Output: 
```
{
    "Response": {
        "Columns": [
            {
                "Description": "",
                "ExtParameters": null,
                "Length": 0,
                "Name": "id",
                "Position": 2,
                "Precision": 0,
                "Scale": 0,
                "Type": "int"
            }
        ],
        "DbName": "db1",
        "Description": "",
        "ExtParameters": null,
        "Location": "",
        "Name": "t1",
        "Partitions": null,
        "RequestId": "5406b2cc-d2d1-4f56-9f5d-fc0547555d57"
    }
}
```

