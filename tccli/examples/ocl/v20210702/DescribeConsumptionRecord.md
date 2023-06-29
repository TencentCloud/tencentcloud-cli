**Example 1: 获取消费记录**

获取消费记录

Input: 

```
tccli ocl DescribeConsumptionRecord --cli-unfold-argument  \
    --OrgId 12345 \
    --CostType 1 \
    --PageNo 0 \
    --PageSize 1 \
    --EndDay 2020-09-22 \
    --StartDay 2020-09-22
```

Output: 
```
{
    "Response": {
        "Total": 100,
        "Data": [
            {
                "OrgId": 25110000,
                "ClassId": 11630000,
                "ClassName": "k8s分享",
                "ClassType": 1,
                "Used": 1234.56,
                "SubType": 1,
                "UsedType": 1,
                "CostType": 1,
                "CreateTime": "2021-04-20 08:08:08",
                "DealName": "K0000102301225"
            }
        ],
        "RequestId": "ddgdgaadfgddfa"
    }
}
```

