**Example 1: 获取多经点位底图**



Input: 

```
tccli ump DescribeMultiBizBaseImage --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --ZoneId 1 \
    --CameraId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "ImageUrl": "http://youmall.cos.ap-shanghai.myqcloud.com/tmp.png"
    }
}
```

