**Example 1: 资产中心资产树信息**



Input: 

```
tccli cfw DescribeResourceGroup --cli-unfold-argument  \
    --GroupId  \
    --QueryType vpc \
    --ShowType 
```

Output: 
```
{
    "Response": {
        "Data": "[{\"GroupId\":\"1300448058_masternode\",\"ParentId\":\"\",\"GroupName\":\"全部资产\",\"Cidr\":\"\",\"Path\":\"\",\"InsNum\":52,\"TreeChild\":[{\"GroupId\":\"测试A\",\"ParentId\":\"\",\"GroupName\":\"测试A\",\"Cidr\":\"\",\"Path\":\"\",\"InsNum\":3,\"TreeChild\":[{\"GroupId\":\"测试A%cfw%测试B\",\"ParentId\":\"\",\"GroupName\":\"测试B\",\"Cidr\":\"\",\"Path\":\"\",\"InsNum\":3,\"TreeChild\":[]}]},]}]",
        "RequestId": ""
    }
}
```

