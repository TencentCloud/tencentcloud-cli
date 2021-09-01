**Example 1: 查询路由列表**

查询路由列表

Input: 

```
tccli bmvpc DescribeRouteTables --cli-unfold-argument  \
    --RouteTableIds rtb-q1j48dkd
```

Output: 
```
{
    "Response": {
        "RouteTableSet": [
            {
                "VpcId": "vpc-lqrdo8yu",
                "RouteTableId": "rtb-19yps3nz",
                "RouteTableName": "default",
                "VpcName": "test",
                "VpcCidrBlock": "10.1.0.0/16",
                "Zone": "ap-guangzhou-h3-1",
                "CreateTime": "2019-01-02 15:05:26"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c2e7a91b-e358-4391-acc0-9f0cd57bd971"
    }
}
```

