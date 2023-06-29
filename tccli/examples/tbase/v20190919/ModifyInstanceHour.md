**Example 1: TbaseV2后付费变配实例**



Input: 

```
tccli tbase ModifyInstanceHour --cli-unfold-argument  \
    --ModifyType 3 \
    --NodeType 1 \
    --Zone ap-guangzhou-2 \
    --InstanceId tdpg-taagd2g3 \
    --Storage 100 \
    --SetCount 3 \
    --SpecCode dev.cn.1 \
    --NodeCount 8
```

Output: 
```
{
    "Response": {
        "BillId": "20201128129000007109331",
        "RequestId": "4fe4c3b6-87f6-49b2-adee-3e604cf7b016"
    }
}
```

