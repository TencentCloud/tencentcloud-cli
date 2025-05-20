**Example 1: 查询 VPC 详细信息**



Input: 

```
tccli lighthouse DescribeVpcsInternal --cli-unfold-argument  \
    --VpcIds vpc-nzpgrbrj \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VpcSet": [
            {
                "VpcId": "vpc-nzpgrbrj",
                "AppId": 251010674
            }
        ],
        "RequestId": "ac5b2e80-bc71-4c48-be07-10abedced7dd"
    }
}
```

