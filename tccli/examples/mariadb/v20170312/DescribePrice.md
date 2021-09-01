**Example 1: 查询新购云数据库实例的价格**



Input: 

```
tccli mariadb DescribePrice --cli-unfold-argument  \
    --NodeCount 2 \
    --Memory 2000 \
    --Storage 10000 \
    --Zone ap-guangzhou-2 \
    --Count 1 \
    --Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7e1000c2-190a-d0df-ff75-59fbdf5ff381",
        "OriginalPrice": 21120,
        "Price": 21120
    }
}
```

