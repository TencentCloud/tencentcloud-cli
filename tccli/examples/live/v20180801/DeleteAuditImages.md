**Example 1: 直播审核图库删除图片**



Input: 

```
tccli live DeleteAuditImages --cli-unfold-argument  \
    --ImageIds 75500dac4340c9973f90e24331c07127_100
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "ErrMsg": "",
                "ImageId": "75500dac4340c9973f90e24331c07127_100",
                "Label": "Normal",
                "Name": "autotest_HLRIioUifQ.jpeg",
                "Status": 0
            }
        ],
        "RequestId": "474bee92-37cb-4645-9f7b-b77ba014c6ef"
    }
}
```

