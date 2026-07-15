**Example 1: 开通 TWeSee 视频理解后付费**



Input: 

```
tccli iotexplorer CreateTWeSeePostPaidService --cli-unfold-argument  \
    --ServiceType VID_COMP
```

Output: 
```
{
    "Response": {
        "OrderId": "20260417*********427251",
        "ResourceId": "twesee-753yd29x1u********g0we9",
        "Status": "DELIVERED",
        "RequestId": "f05a6c5a-cf05-4781-a106-ca74957f6580"
    }
}
```

**Example 2: 开通 TWeSee 图片理解后付费**



Input: 

```
tccli iotexplorer CreateTWeSeePostPaidService --cli-unfold-argument  \
    --ServiceType IMG_COMP
```

Output: 
```
{
    "Response": {
        "OrderId": "20260420********4271701",
        "ResourceId": "twesee-753yd29x2z********rdlaa",
        "Status": "DELIVERED",
        "RequestId": "2f542310-6c2e-4a65-86a9-f8dbf02cbc87"
    }
}
```

