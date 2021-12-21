**Example 1: 线索回收接口**



Input: 

```
tccli wav CreateLead --cli-unfold-argument  \
    --SeriesId 1376410380566495234 \
    --SalesName 李四 \
    --Remark 备注 \
    --ChannelName 51QC \
    --DealerId 1438394065134600193 \
    --SourceType 0 \
    --CustomerSex 0 \
    --ChannelId 1008 \
    --BrandId 1373911438101237762 \
    --CustomerPhone 手机号 \
    --SalesPhone 手机号 \
    --CcName 王五 \
    --ModelId 1376759329958998019 \
    --CreateTime 1638178594245 \
    --CustomerName 张三
```

Output: 
```
{
    "Response": {
        "RequestId": "fea177dd-9fa6-4e76-9c8f-67f5a21f20bb",
        "BusinessCode": 0,
        "BusinessMsg": "创建成功"
    }
}
```

