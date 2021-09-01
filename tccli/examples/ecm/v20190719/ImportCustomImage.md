**Example 1: 导入自定义镜像**



Input: 

```
tccli ecm ImportCustomImage --cli-unfold-argument  \
    --ImageDescription description \
    --ImageName ecmtest \
    --Architecture x86_64 \
    --OsType CentOS \
    --OsVersion 7.6 \
    --ImageUrls.0.ImageFile https://images-1251557890.cos.ap-chengdu.myqcloud.com/images/img2019080706034135/img2019080706034135.qcow2 \
    --ImageUrls.1.ImageFile https://images-1251557890.cos.ap-chengdu.myqcloud.com/images/img2018091002367608/img2018091002367608.qcow2
```

Output: 
```
{
    "Response": {
        "ImageId": "img-c1p90f6q",
        "TaskId": 21,
        "RequestId": "93cba77c-fc19-43fe-9b57-dabe5035ffb7"
    }
}
```

