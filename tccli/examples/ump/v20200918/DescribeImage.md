**Example 1: 获取底图**



Input: 

```
tccli ump DescribeImage --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --CameraId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "ImageUrl": "http://youmall.cos.ap-shanghai.myqlcoud.com/123456.png"
    }
}
```

