**Example 1: 查询 TWeSee 图片理解后付费服务**



Input: 

```
tccli iotexplorer DescribeTWeSeePostPaidService --cli-unfold-argument  \
    --ServiceType IMG_COMP
```

Output: 
```
{
    "Response": {
        "ResourceId": "twesee-753yd29x2z********rdlaa",
        "Status": "NORMAL",
        "RequestId": "f8c3d6d1-5c9f-4f2d-b83d-82385a734a5e"
    }
}
```

**Example 2: 查询 TWeSee 视频理解后付费服务**



Input: 

```
tccli iotexplorer DescribeTWeSeePostPaidService --cli-unfold-argument  \
    --ServiceType VID_COMP
```

Output: 
```
{
    "Response": {
        "ResourceId": "twesee-753yd29x1u********g0we9",
        "Status": "NORMAL",
        "RequestId": "dea01d1e-53bd-4900-b25e-bf764b94b11b"
    }
}
```

