**Example 1: 获取投递详情**



Input: 

```
tccli config DescribeAggregateConfigDeliver --cli-unfold-argument  \
    --AccountGroupId ca-sdfs7734h24
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "DeliverType": "COS",
        "DeliverPrefix": "testPrefix",
        "DeliverName": "testDeliver",
        "TargetArn": "qcs::cos:ap-guangzhou:700000358201:prefix/251227028/testbucket-251237532/0",
        "CreateTime": "2023-12-12 20:23:56",
        "DeliverUin": 700000591517,
        "RequestId": "77c49fca-aa2c-471b-a5d6-d62496f2d13b"
    }
}
```

