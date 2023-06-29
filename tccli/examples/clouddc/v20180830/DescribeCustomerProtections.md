**Example 1: 示例**



Input: 

```
tccli clouddc DescribeCustomerProtections --cli-unfold-argument  \
    --CustomerName 姚晓城 \
    --SearchType equal
```

Output: 
```
{
    "Response": {
        "JsonString": "{\"list\":[{\"id\":110055,\"protectionType\":5,\"areaId\":-1,\"saleCenter\":\"\",\"isLimitSale\":0,\"salesGroupName\":\"\",\"customerName\":\"\\u59da\\u6653\\u57ce\",\"customerShortName\":\"\",\"cid\":\"\",\"associatedCustomers\":\"\",\"industryId\":-1,\"secondaryIndustryId\":-1,\"businessManager\":\"\",\"preBusinessManager\":\"\",\"remark\":\"\",\"addUser\":\"v_atzzhang\",\"updateUser\":\"v_atzzhang\",\"createTime\":\"2021-03-15 17:02:51\",\"updateTime\":\"2021-03-15 17:03:28\",\"preSalesGroupName\":\"\",\"preSalesCenter\":\"\",\"districtBelong\":\"\\u4e0d\\u533a\\u5206\\u533a\\u57df\",\"industryName\":\"\\u4e0d\\u533a\\u5206\\u4e00\\u7ea7\\u884c\\u4e1a\",\"secondaryIndustryName\":\"\\u4e0d\\u533a\\u5206\\u4e8c\\u7ea7\\u884c\\u4e1a\",\"protectionName\":\"svip\\u4fdd\\u62a4\\u6c60\"}],\"total\":1}",
        "RequestId": "890c7f1a-cccd-48b6-a9d5-314e01a232ce"
    }
}
```

