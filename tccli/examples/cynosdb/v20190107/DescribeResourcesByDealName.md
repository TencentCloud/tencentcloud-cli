**Example 1: 查询订单id关联的资源信息**



Input: 

```
tccli cynosdb DescribeResourcesByDealName --cli-unfold-argument  \
    --DealName xxx
```

Output: 
```
{
    "Response": {
        "BillingResourceInfos": [
            {
                "ClusterId": "cynosdbmysql-r8ewihg4",
                "InstanceIds": [
                    "cynosdbmysql-ins-pecl0drs"
                ],
                "DealName": "xxx"
            },
            {
                "ClusterId": "cynosdbmysql-hjosrxhu",
                "InstanceIds": [
                    "cynosdbmysql-ins-7f59pahg"
                ],
                "DealName": "xxx"
            }
        ],
        "RequestId": "005b862f-f408-4a95-a7e7-26f3e672e081"
    }
}
```

