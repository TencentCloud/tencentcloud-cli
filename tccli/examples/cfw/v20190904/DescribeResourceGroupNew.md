**Example 1: 资产中心资产组数数据信息查询**

资产中心资产组数数据信息查询

Input: 

```
tccli cfw DescribeResourceGroupNew --cli-unfold-argument  \
    --GroupId cfwrg-****node \
    --QueryType resource \
    --ShowType all
```

Output: 
```
{
    "Response": {
        "Data": "[{\"GroupId\":\"cfwrg-130044******node\",\"ParentId\":\"0\",\"GroupName\":\"全部资产\",\"Cidr\":\"mastercidr\",\"Path\":\"/全部资产/\",\"InsNum\":52,\"TreeChild\":[{\"GroupId\":\"cfwrg-17***********349477\",\"ParentId\":\"cfwrg-1300448058masternode\",\"GroupName\":\"clay\",\"Cidr\":\"mastercidr\",\"Path\":\"/全部资产/clay/\",\"InsNum\":1,\"TreeChild\":[]}]}]",
        "RequestId": "60e4d0ea-f89a-4cfa-b132-64449c7e894a",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "UnResourceNum": 5
    }
}
```

