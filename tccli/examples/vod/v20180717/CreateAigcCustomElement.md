**Example 1: 请求示例**



Input: 

```
tccli vod CreateAigcCustomElement --cli-unfold-argument  \
    --ElementName my_element \
    --ElementDescription 主体 \
    --ElementFrontalImage https://****.vod-qcloud.com/6cd2c44bvodcq1500039**/179cafb25145403**1/ClcdjoxE6jcA.png \
    --ElementReferList.0.ImageUrl https://****.vod-qcloud.com/6cd2c44bvodcq1500039**/179cafb25145403**1/feefsfrefer.png
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "ElementId": "53459345344333"
    }
}
```

