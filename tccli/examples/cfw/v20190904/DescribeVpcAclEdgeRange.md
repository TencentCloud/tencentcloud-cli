**Example 1: 查询内网间访问控制规则的生效范围**

查询内网间访问控制规则的生效范围示例

Input: 

```
tccli cfw DescribeVpcAclEdgeRange --cli-unfold-argument  \
    --FromList rules \
    --Filters.0.Name EdgeId \
    --Filters.0.Values cfws-xxxx \
    --Filters.0.OperatorType 9 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "EdgeRanges": [
            {
                "EdgeId": "cfws-xxx",
                "EdgeName": "test",
                "SrcId": "vpc-xxx",
                "SrcRegion": "ap-shanghai",
                "SrcName": "test1",
                "SrcCidr": "192.168.0.0/24",
                "DstId": "vpc-xxx",
                "DstRegion": "ap-shanghai",
                "DstName": "test2",
                "DstCidr": "192.168.2.0/24"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

