**Example 1: 测试示例1**

测试示例1

Input: 

```
tccli tchousex DescribeTableList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993 \
    --DbName db1
```

Output: 
```
{
    "Response": {
        "RequestId": "6658b463-d363-4867-b87a-e2428f6b95fc",
        "Tables": [
            {
                "DbName": "db1",
                "Name": "t1",
                "Type": "table"
            },
            {
                "DbName": "db1",
                "Name": "t2",
                "Type": "table"
            },
            {
                "DbName": "db1",
                "Name": "t4",
                "Type": "table"
            },
            {
                "DbName": "db1",
                "Name": "tt2",
                "Type": "table"
            },
            {
                "DbName": "db1",
                "Name": "v1",
                "Type": "view"
            },
            {
                "DbName": "db1",
                "Name": "v2",
                "Type": "view"
            },
            {
                "DbName": "db1",
                "Name": "v3",
                "Type": "view"
            }
        ],
        "TotalCount": 7
    }
}
```

