**Example 1: 获取图片优化的配置**



Input: 

```
tccli cdn DescribeImageConfig --cli-unfold-argument  \
    --Domain test.tencent.com
```

Output: 
```
{
    "Response": {
        "WebpAdapter": {
            "Switch": "on/off"
        },
        "TpgAdapter": {
            "Switch": "on/off"
        },
        "GuetzliAdapter": {
            "Switch": "on/off"
        },
        "AvifAdapter": {
            "Switch": "on/off"
        },
        "RequestId": "29699aac-9898-4baf-b645-7cc31d972674"
    }
}
```

