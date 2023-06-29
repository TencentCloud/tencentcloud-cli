**Example 1: 查询码包地址**



Input: 

```
tccli trp DescribeCodePackUrl --cli-unfold-argument  \
    --PackId 1d7288c8-e1d8
```

Output: 
```
{
    "Response": {
        "FileKey": "anxin/1d8-4460-81f6e509e048.zip",
        "Url": "https://anxin-private-1251316161.cos.ap-guangzhou.myqcloud.com/anxin/1d8-4460-81f6e509e048.zip",
        "ImgUrl": "https://anxin-private-1251316161.cos.ap-guangzhou.myqcloud.com/anxin/1d8-4460-81f6e509e048_qr.zip",
        "RequestId": "d8dca787-f07a-40ce-acd5-3c0eda11cac2"
    }
}
```

