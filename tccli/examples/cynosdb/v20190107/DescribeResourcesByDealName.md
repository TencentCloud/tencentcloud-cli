**Example 1: 查询订单关联实例**



Input: 

```
tccli cynosdb DescribeResourcesByDealName --cli-unfold-argument  \
    --DealName 201302542054
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

