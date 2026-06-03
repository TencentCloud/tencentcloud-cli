**Example 1: 添加serverless只读实例**



Input: 

```
tccli cynosdb AddServerlessRoInstances --cli-unfold-argument  \
    --ClusterId cynosdbmysql-oi7mh90n \
    --MinCpu 1 \
    --MaxCpu 2 \
    --InstanceName S1-db-环境1 \
    --Port 3306 \
    --RoCount 1
```

Output: 
```
{
    "Response": {
        "BigDealIds": null,
        "DealNames": [
            "20260509445022752472821"
        ],
        "ResourceIds": [
            "cynosdbmysql-ins-p1hpv1kk"
        ],
        "TranId": "20260509445022752472831",
        "RequestId": "29c45fc5-79bd-4794-91c0-50717b7978aa"
    }
}
```

