**Example 1: PropOwnerCertOCR调用**



Input: 

```
tccli ocr PropOwnerCertOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "Owner": "李明",
        "Possession": "单独所有",
        "RegisterTime": "2015-02-22",
        "Purpose": "成套住宅",
        "Nature": "商品房",
        "Location": "上海市徐汇区田林路397号腾云大厦",
        "RequestId": "67c12150-b6e4-41a0-a404-503fe83d7e85"
    }
}
```

