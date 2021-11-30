**Example 1: 获取私有域解析账号的VPC列表**



Input: 

```
tccli privatedns DescribeAccountVpcList --cli-unfold-argument  \
    --AccountUin 123456789 \
    --Limit 200 \
    --Offset 0 \
    --Filters.0.Name Region \
    --Filters.0.Values ap-guangzhou \
    --Filters.1.Name VpcName \
    --Filters.1.Values test \
    --Filters.2.Name VpcId \
    --Filters.2.Values vpc-sdfwadf1
```

Output: 
```
{
    "Response": {
        "RequestId": "443f1f2b-9be4-4a2c-b1a6-0494c2d980ff",
        "TotalCount": 1,
        "VpcSet": [
            {
                "VpcId": "vpc-ofnocfe1",
                "VpcName": "testname",
                "Uin": 700000136857,
                "Region": "ap-guangzhou"
            }
        ]
    }
}
```

