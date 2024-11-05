**Example 1: 资产中心资产树信息**



Input: 

```
tccli cfw DescribeResourceGroup --cli-unfold-argument  \
    --GroupId 0 \
    --QueryType vpc \
    --ShowType ALL
```

Output: 
```
{
    "Response": {
        "Data": "[{\"GroupId\":\"1300448058_masternode\",\"ParentId\":\"masternodeall\",\"GroupName\":\"全部资产\",\"Cidr\":\"cidrmaster\",\"Path\":\"masternode\",\"InsNum\":52,\"TreeChild\":[{\"GroupId\":\"测试A\",\"ParentId\":\"1300448058_masternode\",\"GroupName\":\"测试A\",\"Cidr\":\"cidrmaster\",\"Path\":\"master\",\"InsNum\":3,\"TreeChild\":[{\"GroupId\":\"测试A%cfw%测试B\",\"ParentId\":\"1300448058_masternode\",\"GroupName\":\"测试B\",\"Cidr\":\"cidrmaster\",\"Path\":\"测试B\",\"InsNum\":3,\"TreeChild\":[]}]}]}]",
        "RequestId": "3bd058eb-d48b-4f41-b1ba-bc5b0bf67eb7"
    }
}
```

